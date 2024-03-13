from django.shortcuts import render
from django.http import HttpResponseRedirect
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from mailchimp_marketing import Client
import os


# Configure Mailchimp
MAILCHIMP_API_KEY = os.environ.get('MAILCHIMP_API_KEY')
MAILCHIMP_SERVER_PREFIX = os.environ.get('MAILCHIMP_SERVER_PREFIX')

mailchimp = Client()
mailchimp.set_config({
    'api_key': MAILCHIMP_API_KEY,
    'server': MAILCHIMP_SERVER_PREFIX,
})


def subscribe_newsletter_view(request):
    """ subscribe to newletter view """

    #set refering page to render correct page after user have subscribed
    request.session['referring_page'] = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        # Extract the email from the form submission
        email = request.POST.get('subscribe-email')

        # Call the subscribe_to_newsletter function
        subscribe_user_to_newsletter(email)

        # Call send newletter function
        send_newsletter(email)

        referring_page = request.session.get('referring_page', '/')
        return HttpResponseRedirect(referring_page)

    return render(request, 'home/index.html')

def subscribe_user_to_newsletter(email):
    """ Add the email to the audience to mailchimp """
    try:
        # Add user to your Mailchimp audience
        audience_id = '8fbb67c234' 
        body = {
            'email_address': email,
            'status': 'subscribed',
        }
        response = mailchimp.lists.add_list_member(audience_id, body)

        print(f"User subscribed successfully: {response}")

    except ApiClientError as e:
        print(f"Error subscribing user: {e.text}")

def send_newsletter(email):
    ''' Send the email with the desiered campaigns '''
    try:
        # Get the target campaign IDs from the environment variable
        target_campaigns = os.environ.get('TARGET_CAMPAIGNS', '').split(',')


        # Find and send campaigns based on the specified IDs
        for campaign_id in target_campaigns:
            try:
                
                # Send the campaign
                mailchimp.campaigns.send(campaign_id)
                
                print(f"Newsletter sent successfully. Campaign ID: {campaign_id}")
                
            except ApiClientError as e:
                print(f"Error sending newsletter for campaign ID {campaign_id}: {e.text}")


    except ApiClientError as e:
        print(f"Error sending newsletter: {e.text}")


def index(request):
    """ View that returns the index page """
    
    return render(request, 'home/index.html')

def custom_404_view(request, exception):
    ''' render 404 page '''
    #This custom 404 view i never called have tried alot of different apporaches..
    print("call 404")
    return render(request, '404.html', status=404)
    