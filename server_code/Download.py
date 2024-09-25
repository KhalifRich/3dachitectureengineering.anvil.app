import anvil.secrets
import stripe
from datetime import datetime
import anvil.server

stripe.api_key = "pk_live_51OVEBOJSA1HIvKzyhEGFtfRsONEJamAarke1ATOOWUArEtao908p1R0l4VtBZiTCsNfpWSqOpuYo0e41P63gGMwC00iTLg0sNK"

@anvil.server.callable
def download_project(user_email, project_id, quoted_price):
    user = app_tables.users.get(email=user_email)
    project = app_tables.projects.get_by_id(project_id)
    engineer = project['user']
    
    if user and project and engineer:
        download_price = int(quoted_price * 100)  # Convert dollars to cents
        engineer_share = download_price // 2
        admin_share = download_price - engineer_share

        # Transfer to engineer
        try:
            transfer = stripe.Transfer.create(
                amount=engineer_share,
                currency="usd",
                destination=engineer['stripe_account_id'],
                transfer_group="PROJECT_DOWNLOAD"
            )
            # Update engineer balance
            engineer['balance'] = (engineer['balance'] or 0) + engineer_share

            # Log the download
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
