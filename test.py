import smtplib
import psutil     #psutil - https://github.com/giampaolo/psutil

list = psutil.pids()

# Go though list and check each processes executeable name for 'putty.exe'
while True:

    for i in range(0, len(list)):
        try:
            p = psutil.Process(list[i])
            if p.cmdline()[0].find("AcroRd32.exe") != -1:
                # PuTTY found. Kill it
                p.kill()
                break;
        except:
            pass




"""smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('Your email', 'Your password')
smtpObj.sendmail('Your email', 'Your email', 'Subject: Solong.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtpObj.quit()"""
