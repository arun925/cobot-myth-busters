from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def home():
    return "'Hello 🙋🏽‍♂, \nThis is a Covid-whatsapp-Bot to provide latest information updates, self check on symptoms and identifying fake news .\n For any emergency 👇 \n 📞 Helpline: 011-23978046 | Toll-Free Number: 1075 \n ✉ Email: ncov2019@gov.in \n\n Please enter one of the following option 👇 \n *A*. Covid-19 statistics *Worldwide*. \n *B*. Covid-19 cases in *India*.  \n *C*. Statewise statistics in India. \n *D*. self-analysis. \n *E*. Identify Fake news \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken. \n *H*. *Contact Details - State wise."


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'Hi' in incoming_msg or 'Hey' in incoming_msg or 'Menu' in incoming_msg:
        text = f'Hello 🙋🏽‍♂, \nThis is a Covid-whatsapp-Bot to provide latest information updates, self check on symptoms and identifying fake news .\n For any emergency 👇 \n 📞 Helpline: 011-23978046 | Toll-Free Number: 1075 \n ✉ Email: ncov2019@gov.in \n\n Please enter one of the following option 👇 \n *A*. *Fake news* Identification (Myth Busters) \n *B*. *Self-Assessment* for COVID symptoms. \n *C*. Covid-19 statistics *Worldwide*. \n *D*. Covid-19 cases in *India*.  \n *E*. How does it *Spread*?'
        msg.body(text)
        responded = True

    if 'C' in incoming_msg:
        r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases Worldwide_ \n\nConfirmed Cases : *{data["cases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}*  \n\n 👉 Type *B* to check cases in *India* \n 👉 Type *B, C, D, E, F, G* to see other options \n 👉 Type *Menu* to view the Main Menu'
        else:
            text = 'Could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    if 'D' in incoming_msg or 'India' in incoming_msg:
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/india')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in India_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n 👉 Type *A, C, D, E, F, G* to see other options \n 👉 Type *Menu* to view the Main Menu'
        else:
            text = 'Could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    # if 'E' in incoming_msg in incoming_msg:
    #     r = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
    #     if r.status_code == 200:
    #         data = r.json()
    #         text = f'_Covid-19 Cases in Andhra_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}* \n\n 👉 Type *D* to check cases in *USA* \n 👉 Type *A, B, D, E, F* to see other options \n 👉 Type *Menu* to view the Main Menu'
    #     else:
    #         text = 'Could not retrieve the results at this time, sorry.'
    #     msg.body(text)
    #     responded = True

    if 'B' in incoming_msg:
        text = 'Self Analysis coming soon.. Sorry for the inconvenience'
        msg.body(text)
        responded = True

    if 'A' in incoming_msg:
        text = f'👇 Choose any below options to get the correct news on few myths (Source WHO (Myth busters))\n *1*. Do you still believe *hot/humid* climate does not spread Corona ? ' \
               f' \n *2*. Does *Cold weather and snow* CANNOT kill the new coronavirus. \n *3*. Taking *hot bath* to kill virus ? ' \
               f' \n *4*. Afraid that *mosquito bites* spreads virus ?*.  \n *5*. Are *hand dryers* effective in killing the new coronavirus?. \n *6*. Can an *ultraviolet disinfection lamp* kill the new coronavirus?. ' \
               f' \n *7*. How effective are *thermal scanners* in detecting people infected with the new coronavirus?. \n *8*. Can *spraying alcohol or chlorine* all over your body kill the new coronavirus?. ' \
               f' \n *9*. Do *vaccines against pneumonia* protect you against the new coronavirus?. \n*10*. Can regularly *rinsing your nose with saline* help prevent infection with the new coronavirus? ' \
               f' \n *11*. Can *eating garlic* help prevent infection with the new coronavirus? \n *12*. Does the new coronavirus *affect older people, or are younger people also susceptible?*. ' \
               f' \n *13*. Are *antibiotics effective in preventing* and treating the new coronavirus? \n *14* Are there *any specific medicines* to prevent or treat the new coronavirus? \n '
        msg.body(text)
        responded = True

    if '1' in incoming_msg:
        text = f'👇 Choose any below options to get the correct news on few myths (Source WHO (Myth busters))\n *1*. Do you still believe *hot/humid* climate does not spread Corona ? ' \
               f' \n *2*. Does *Cold weather and snow* CANNOT kill the new coronavirus. \n *3*. Taking *hot bath* to kill virus ? ' \
               f' \n *4*. Afraid that *mosquito bites* spreads virus ?*.  \n *5*. Are *hand dryers* effective in killing the new coronavirus?. \n *6*. Can an *ultraviolet disinfection lamp* kill the new coronavirus?. ' \
               f' \n *7*. How effective are *thermal scanners* in detecting people infected with the new coronavirus?. \n *8*. Can *spraying alcohol or chlorine* all over your body kill the new coronavirus?. ' \
               f' \n *9*. Do *vaccines against pneumonia* protect you against the new coronavirus?. \n*10*. Can regularly *rinsing your nose with saline* help prevent infection with the new coronavirus? ' \
               f' \n *11*. Can *eating garlic* help prevent infection with the new coronavirus? \n *12*. Does the new coronavirus *affect older people, or are younger people also susceptible?*. ' \
               f' \n *13*. Are *antibiotics effective in preventing* and treating the new coronavirus? \n *14* Are there *any specific medicines* to prevent or treat the new coronavirus? \n '
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/52.tmb-1920v.png?sfvrsn=862374e_1')
        msg.body(text)
        responded = True
    if '2' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/web-mythbusters/mb-cold-snow.tmb-1920v.png?sfvrsn=1e557ba_1')
        responded = True
    if '3' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/web-mythbusters/mb-hot-bath.tmb-1920v.png?sfvrsn=f1ebbc_1')
        responded = True
    if '4' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/web-mythbusters/mb-mosquito-bite.tmb-1920v.png?sfvrsn=a1d90f6_1')
        responded = True
    if '5' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/web-mythbusters/mythbusters-27.tmb-1920v.png?sfvrsn=d17bc6bb_1')
        responded = True
    if '6' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/mythbusters-31.tmb-1920v.png?sfvrsn=e5989655_1')
        responded = True
    if '7' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/web-mythbusters/mythbusters-25.tmb-1920v.png?sfvrsn=d3bf829c_2')
        responded = True
    if '8' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/web-mythbusters/mythbusters-33.tmb-1920v.png?sfvrsn=47bfd0aa_2')
        responded = True
    if '9' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/web-mythbusters/11.tmb-1920v.png?sfvrsn=97f2a51e_2')
        responded = True
    if '10' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/23.tmb-1920v.png?sfvrsn=c65dad38_3')
        responded = True
    if '11' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/19.tmb-1920v.png?sfvrsn=52adfc93_3')
        responded = True
    if '12' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/mythbuster-2.tmb-1920v.png?sfvrsn=635d24e5_3')
        responded = True
    if '13' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/mythbuster-3.tmb-1920v.png?sfvrsn=10657e42_3')
        responded = True
    if '14' in incoming_msg:
        msg.media(
            'https://www.who.int/images/default-source/health-topics/coronavirus/myth-busters/web-mythbusters/mythbuster-4.tmb-1920v.png?sfvrsn=e163bada_3')
        responded = True
    if 'E' in incoming_msg:
        text = f'_Coronavirus spreads from an infected person through_ 👇 \n\n ♦ Small droplets from the nose or mouth which are spread when a person coughs or sneezes \n\n ♦ Touching an object or surface with these droplets on it and then touching your mouth, nose, or eyes before washing your hands \n \n ♦ Close personal contact, such as touching or shaking hands \n Please watch the video for more information 👇 https://youtu.be/0MgNgcwcKzE \n\n 👉 Type G to check the *Preventive Measures* \n 👉 Type *A, B, C, D, E* to see other options \n 👉 Type *Menu* to view the Main Menu'
        msg.body(text)
        msg.media(
            'https://user-images.githubusercontent.com/34777376/77290801-f2421280-6d02-11ea-8b08-fdb516af3d5a.jpeg')
        responded = True

    # if 'G' in incoming_msg:
    #     text = f'_Coronavirus infection can be prevented through the following means_ 👇 \n ✔️ Clean hand with soap and water or alcohol-based hand rub \n https://youtu.be/EJbjyo2xa2o \n\n ✔️ Cover nose and mouth when coughing & sneezing with a tissue or flexed elbow \n https://youtu.be/f2b_hgncFi4 \n\n ✔️ Avoid close contact & maintain 1-meter distance with anyone who is coughing or sneezin \n https://youtu.be/mYyNQZ6IdRk \n\n ✔️ Isolation of persons traveling from affected countries or places for at least 14 day \n https://www.mohfw.gov.in/AdditionalTravelAdvisory1homeisolation.pdf \n\n ✔️ Quarantine if advise \n https://www.mohfw.gov.in/Guidelinesforhomequarantine.pdf \n\n 👉 Type *A, B, C, D, E, F* to see other option \n 👉 Type *Menu* to view the Main Menu'
    #     msg.body(text)
    #     msg.media(
    #         'https://user-images.githubusercontent.com/34777376/77290864-1c93d000-6d03-11ea-96fe-18298535d125.jpeg')
    #     responded = True

    if responded == False:
        msg.body('I only know about corona virus, sorry!')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
