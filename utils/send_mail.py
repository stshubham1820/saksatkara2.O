import boto3
from botocore.exceptions import ClientError
from saksatkara.settings import SENDER_MAIL,AWS_SECRET_ACCESS_KEY,AWS_REGION,AWS_ACCESS_KEY_ID

class SendMail:
    def __init__(self,subject,recipient_list,body_text,body_html) -> None:
        self.recipient_list = recipient_list
        self.subject = subject
        self.body_text = body_text
        self.body_html = body_html

    def sendMail(self):

        CHARSET = "UTF-8"

        client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': self.recipient_list,
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': self.body_html,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': self.body_text,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': self.subject,
                    },
                },
                Source=SENDER_MAIL,
                # If you are not using a configuration set, comment or delete the
                # following line
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
