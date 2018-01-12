askUserOS = input('do you use windows, mac, ubuntu or mint? yes or no. ').strip()

if askUserOS.lower() in ['y', 'yes']:
    userOS = input('out of the four operating systems above what operating system do you use? ').lower()

if userOS == 'mac':
    print('mac is beter than windows.')
    versionAsk = input('what version of mac are you using? ')
    if versionAsk.lower() in ['10.13 high sierra', 'high sierra', 'high sierra 10.13', '10.13']:
        print('you are using the latest version of mac!')
    else:
        print('you are not using the latest version of mac.')
elif userOS == 'windows':
    print('windows stinkows.')
    versionAsk = input('what version of windows are you using? ')
    if versionAsk.lower() in ['windows 10', 'windows 7']:
        print('you are using the latest version of windows.')
    else:
        print('you are not using the latest version of windows.')
elif userOS == 'ubuntu':
    print('you have a good CPU.')
    versionAsk = input('what version of ubuntu are you using? ')
    if versionAsk.lower() in ['ubuntu 16.04.3 xenial xerus', 'xenial xerus ubuntu 16.04.3', 'xenial xerus', 'ubuntu 16.04.3' ]:
        print('you are using the latest version of ubuntu!')
    else:
        print('you are not using the latest version of ubuntu.')
elif userOS == 'mint':
    print('error your CPU is to low to run this program.')
    versionAsk = input('what version of mint are you using? ')
    if versionAsk.lower() in ['18.3 sylvia ubuntu xenial', 'ubuntu xenial', '18.3', 'sylvia']:
        print('you are using the latest version of mint.')
    else:
        print('you are not using the latest version of mint.')
