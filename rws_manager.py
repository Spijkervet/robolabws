import pandas as pd
import urllib
import pwd
from datetime import datetime
from send_mail import send_mail
from requests import get
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format('.', 'output')),
        logging.StreamHandler()
    ])


def check_username(user):
    try:
        return pwd.getpwnam(user)
    except KeyError:
        return None

def create_notice(name, ip, pwd_user, project, begin_date, end_date):
    notice = """
    Dear {name},<br/><br/>
    Your account with username <b>{pwd_user}</b> on the RobolabWS system ({ip}) has reached its expiration date ({end_date}).<br/><br/>
    It will be on hold for <b>1 month</b> for you to make a copy of your project data. Do not forget any files you stored in the <b>/storage</b> folder.
    <b>Let us know if you are not planning to backup your files.</b> You will be able to login to your account with read-only rights using: <br/><br/>


    <code>
        ssh {pwd_user}@{ip}
    </code>
    <br/><br/><br/>


    To transfer your home folder to your local machine in the <b>robolabws_backup</b> folder, use:<br/><br/>
    <code>
        scp -r {pwd_user}@{ip}:/home/{pwd_user}/ robolabws_backup
    </code>
    <br/><br/>

    Below, you fill find the project description for which you have used the RobolabWS resources.<br/>
    If you would like to extend the usage of your account, please make a new request <a href="https://docs.google.com/forms/d/e/1FAIpQLSeBFQ6H5mI1HdrVGu5hZnbhR0hav_J8z7lzoNLFALjegU0Vuw/viewform">here</a>.<br/><br/>

    Kind regards,<br/>

    The RobolabWS Team<br/><br/><br/>


    --<br/>
    Your project description:<br/>
    {project}
    """.format(name=name, pwd_user=pwd_user, ip=ip, end_date=end_date, project=project)
    return notice


def check_expiration():
    for i, d in df.iterrows():
        if d['Timeframe (end-date)'] < datetime.now():
            if not pd.isnull(d['user']):
                pwd_user = check_username(d['user'])
                if pwd_user:
                    on_hold = d['on_hold']
                    name = d['Your full name and those of your partners (if applicable)']
                    email = d['E-mailadres']
                    project = d['Project Abstract']
                    begin_date = d['Timeframe (start-date)']
                    end_date = d['Timeframe (end-date)']

                    if not on_hold:
                        logger.info('Sent expiration notice to: {}'.format(email))
                        notice = create_notice(name, system_ip, pwd_user.pw_name, project, begin_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
                        send_mail(email, '[Robolab-users] Account Expiration Notice', notice)


if __name__ == '__main__':
    logger = logging.getLogger()
    system_ip = get('https://api.ipify.org').text

    # Get latest robolabws sheet:
    urllib.request.urlretrieve('https://docs.google.com/spreadsheets/d/1muPp6AZqNOZQ_xeWtg2oWcGoanu9gLL5sK2p4UmIjHs/export?format=csv&id=1muPp6AZqNOZQ_xeWtg2oWcGoanu9gLL5sK2p4UmIjHs&gid=507416872', filename='robolabws.csv')
    df = pd.read_csv('robolabws.csv')
    df['Timeframe (start-date)'] = pd.to_datetime(df['Timeframe (start-date)'])
    df['Timeframe (end-date)'] = pd.to_datetime(df['Timeframe (end-date)'])

    check_expiration()
