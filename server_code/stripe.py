import anvil.secrets
import stripe
from datetime import datetime
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables

stripe.api_key = "pk_live_51OVEBOJSA1HIvKzyhEGFtfRsONEJamAarke1ATOOWUArEtao908p1R0l4VtBZiTCsNfpWSqOpuYo0e41P63gGMwC00iTLg0sNK"

UPLOAD_CREDIT = 300  # $3 in cents

@anvil.server.callable
def upload_project(user_email, project_title):
    user = app_tables.users.get(email=user_email)
    if user:
        project = app_tables.projects.add_row(user=user, title=project_title, credits_earned=UPLOAD_CREDIT)
        user['balance'] = (user['balance'] or 0) + UPLOAD_CREDIT
        return project
    else:
        raise Exception("User not found")

def download_project(user_email, project_id, quoted_price):
    user = app_tables.users.get(email=user_email)
    project = app_tables.projects.get_by_id(project_id)
    engineer = project['user']
    
    if user and project and engineer:
        download_price = int(quoted_price * 100)  # Convert dollars to cents
        engineer_share = download_price // 2
        admin_share = download_price - engineer_share

        try:
            transfer = stripe.Transfer.create(
                amount=engineer_share,
                currency="usd",
                destination=engineer['stripe_account_id'],
                transfer_group="PROJECT_DOWNLOAD"
            )
            engineer['balance'] = (engineer['balance'] or 0) + engineer_share

            app_tables.downloads.add_row(
                project=project,
                user=user,
                price=download_price,
                download_time=datetime.now()
            )

            return {
                "status": "success",
                "engineer_share": engineer_share,
                "admin_share": admin_share,
                "transfer_id": transfer['id']
            }
        except stripe.error.StripeError as e:
            raise Exception(f"Failed to transfer to engineer: {str(e)}")
    else:
        raise Exception("User or project not found")

def monthly_credit_transfer():
    engineers = app_tables.users.search()
    for engineer in engineers:
        balance = engineer['balance'] or 0
        if balance > 0:
            try:
                transfer = stripe.Transfer.create(
                    amount=balance,
                    currency="usd",
                    destination=engineer['stripe_account_id'],
                    transfer_group="MONTHLY_ENGINEER_PAYOUT"
                )
                engineer['balance'] = 0
                app_tables.transfers.add_row(
                    engineer=engineer,
                    amount=balance,
                    timestamp=datetime.now(),
                    transfer_id=transfer['id']
                )
            except stripe.error.StripeError as e:
                print(f"Failed to transfer to {engineer['email']}: {str(e)}")

@anvil.server.http_endpoint('/stripe/webhook', methods=['POST'])
def stripe_webhook(**payload):
    event = stripe.Event.construct_from(payload, stripe.api_key)

    if event['type'] == 'transfer.created':
        transfer = event['data']['object']
        print(f"Transfer created: {transfer['id']}")
    return "Success"
