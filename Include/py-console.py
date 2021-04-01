from os import system, name
import ctypes
import webbrowser

ctypes.windll.kernel32.SetConsoleTitleW("Command Prompt - Language Selection - Early Acces")

language = str("default")
language2 = str("default")
language3 = str("default")

commandRequire = int
commandRequire = 0;

settingsFileWrite2 = open("langaugeSettings.mqs", "a")
settingsFileWrite2.write("")
settingsFileWrite2.close()

settingsFileRead = open("langaugeSettings.mqs","r")
language2 = settingsFileRead.read()
language = settingsFileRead.read()
settingsFileRead.close()

if (language2 != "tr_TR") and (language2 != "en_US"):
    language = input("PYC >>> Lütfen Dilinizi Giriniz - Please Enter Language (tr_TR veya en_US) (tr_TR or en_US) >>> ")
    language2 = language

    settingsFileWrite = open("langaugeSettings.mqs", "w")
    settingsFileWrite.write(language)
    settingsFileWrite.close()

    ctypes.windll.user32.MessageBoxW(0, "Restart the program to save the changes. - Değişikliklerin kaydedilmesi için programı yeniden başlatınız.", "Warnings - Uyarı", 1)
    quit()


if language2 == "en_US":
    system("clear") if name == "posix" else system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("Command Promt - Main - Early Acces")

    print("Command Prompt")
    print("E/A Version")
    print("This is an open source project. Their codes are shared on GitHub.")
    print("You can learn other commands by entering the !help command")
    print("")
if language2 == "tr_TR":
    system("clear") if name == "posix" else system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("Komut İstemcisi - Ana Temel - Erken Erişim")
    print("Komut İstemcisi")
    print("E/A Sürümü")
    print("Bu proje açık kaynak kodu ile yazılmıştır. Kodlar GitHub üzerinden yayımlanmıştır.")
    print("!yardım ile diğer komutlara ulaşabilirsiniz.")
    print("")

userCommand = str
url1 = str("https://github.com/macesgamesstudios/command-promt-py")

if (language2 == "tr_TR"):
    while commandRequire == 0:
        userCommand = (input("PYC >>> "))
        if (userCommand == "!yardım"):
            print("")
            print("---------- YARDIM ----------")
            print("!yardım -> Komutlar hakkında bilgi verir.")
            print("!dil -> Dil ayarlarını düzenler.")
            print("!hakkında -> Uygulama hakkında bilgi verir.")
            print("!çıkış -> Programdan çıkış yapar.")
            print("!temizle -> Konsol geçmişini temizler.")
            print("!github.link -> Projenin GitHub sayfasını açar.")
            print("-----------------------------")
            print("")
        if (userCommand == "!github.link"):
            print("")
            print("---------- LİNK ----------")
            print("Proje Varsayılan İnternet Tarayıcınızda Açıldı!")
            print("--------------------------")
            print("")
            webbrowser.open(url1, new=0, autoraise=True)
        if (userCommand == "!çıkış"):
            exit()
            print("")
        if (userCommand == "!temizle"):
            if language2 == "en_US":
                system("clear") if name == "posix" else system("cls")
                ctypes.windll.kernel32.SetConsoleTitleW("Command Prompt - Main - Early Acces / v.0.4.2")

                print("Command Prompt")
                print("E/A Version")
                print("This is an open source project. Their codes are shared on GitHub.")
                print("You can learn other commands by entering the !help command")
                print("")
            if language2 == "tr_TR":
                system("clear") if name == "posix" else system("cls")
                ctypes.windll.kernel32.SetConsoleTitleW("Komut İstemcisi - Ana Temel - Erken Erişim")

                print("Komut İstemcisi")
                print("E/A Sürümü")
                print("Bu proje açık kaynak kodu ile yazılmıştır. Kodlar GitHub üzerinden yayımlanmıştır. (!link yazarak GitHub'a ulaşabilirsiniz.)")
                print("!yardım ile diğer komutlara ulaşabilirsiniz.")
                print("")
        if (userCommand == "!hakkında"):
            print("")
            print("---------- HAKKINDA ----------")
            print("Versyon : E/A")
            print("Geliştirici : Maces Games STUDIOS")
            print("Yayımcı : Maces Games STUDIOS")
            print("Uygulama Tipi : Açık Kaynak")
            print("------------------------------")
            print("")
        if (userCommand == "!hesap.makinesi"):
            hesap1 = str();
            hesap2 = int();
            hesap3 = int();

            print("")
            print("---------- HESAP MAKİNESİ ----------")
            print("Lütfen yapmak istediğniz işlem türünü yazınız! (!çarpma - !toplama - !bölme - !çıkarma")
            hesap1 = input("Hesap Makinesi >>> ")
            print("")
            print("Lütfen 1'inci değeri giriniz!")
            print("")
            hesap2 = int(input("Hesap Makinesi >>> "))
            print("")
            print("Lütfen 2'inci değeri giriniz!")
            print("")
            hesap3 = int(input("Hesap Makinesi >>> "))
            print("-------------------------------------")
            print("")

        if (userCommand == "!dil"):
            print("")
            print("---------- DİL ----------")
            print("")
            print("Lütfen Değiştirmek İstediğiniz dili yazınız; (tr_TR veya en_US kodları ile yazınız.) (!iptal yazarak iptal edebilirsiniz!)")
            print("")

            language3 = (input("PYC >>> "))
            if (language3 != "tr_TR" and language3 != "en_US"):
                while (language3 != "tr_TR" and language3 != "en_US"):
                    print("")
                    print("Lütfen geçerli bir dil kodu giriniz!")
                    print("")
                    language3 = (input("PYC >>> "))
            if (language3 == "tr_TR"):
                settingsFileWrite3 = open("langaugeSettings.mqs", "w")
                settingsFileWrite3.write("tr_TR")
                settingsFileWrite3.close()
                ctypes.windll.user32.MessageBoxW(0, "Değişikliklerin aktif olması için programı yeniden başlatınız",
                                                 "Uyarı", 0)
                quit()
            if (language3 == "en_US"):
                settingsFileWrite4 = open("langaugeSettings.mqs", "w")
                settingsFileWrite4.write("en_US")
                settingsFileWrite4.close()
                ctypes.windll.user32.MessageBoxW(0, "Restart the program to save the changes.", "Warnings", 0)
                quit()
            print("")
            print("---------------------------")
            print("")

        if (userCommand != "!yardım" and userCommand != "!dil" and userCommand != "!hakkında" and userCommand != "!çıkış" and userCommand != "!github.link"):
            print("")
            print("---------------------------")
            print("Hatalı Komut!")
            print("---------------------------")
            print("")


if (language2 == "en_US"):
    while commandRequire == 0:
        userCommand = (input("PYC >>> "))
        if (userCommand == "!help"):
            print("")
            print("---------- HELP ----------")
            print("!help -> Provides information about commands.")
            print("!language -> Adjusts the language settings.")
            print("!about -> Gives information about the application.")
            print("!exit -> Exit application.")
            print("!clear -> Clear the console history.")
            print("!github.link -> Opens the project's GitHub page.")
            print("--------------------------")
            print("")
        if (userCommand == "!github.link"):
            print("")
            print("---------- LİNK ----------")
            print("Project Opened in Your Default Internet Browser!")
            print("--------------------------")
            print("")
            webbrowser.open(url1, new=0, autoraise=True)
        if (userCommand == "!exit"):
            exit()
            print("")
        if (userCommand == "!clear"):
            if language2 == "en_US":
                system("clear") if name == "posix" else system("cls")
                ctypes.windll.kernel32.SetConsoleTitleW("mTerminal - Main - Early Acces / v.0.4.2")

                print("mTerminal")
                print("Early Acces - v.0.4.2")
                print("This is an open source project. Their codes are shared on GitHub.")
                print("You can learn other commands by entering the !help command")
                print("")
            if language2 == "tr_TR":
                system("clear") if name == "posix" else system("cls")
                ctypes.windll.kernel32.SetConsoleTitleW("mTerminal - Ana Temel - Erken Erişim / v.0.4.2")

                print("mTerminal")
                print("Erken Erişim - v.0.4.2")
                print("Bu proje açık kaynak kodu ile yazılmıştır. Kodlar GitHub üzerinden yayımlanmıştır. (!link yazarak GitHub'a ulaşabilirsiniz.)")
                print("!yardım ile diğer komutlara ulaşabilirsiniz.")
                print("")
        if (userCommand == "!about"):
            print("")
            print("---------- ABOUT ----------")
            print("Version: EA / v.0.4.2")
            print("Developer : Maces Games STUDIOS")
            print("Publisher : Maces Games STUDIOS")
            print("Application Type: Open Source")
            print("--------------------------")
            print("")
        if (userCommand == "!language"):
            print("")
            print("---------- LANG ----------")
            print("")
            print("Please write the language you want to change; (write with tr_TR or en_US codes.")
            print("")

            language3 = (input("PYC >>> "))
            if (language3 != "tr_TR" and language3 != "en_US"):
                while (language3 != "tr_TR" and language3 != "en_US"):
                    print("")
                    print("Please enter a valid language code!")
                    print("")
                    language3 = (input("PYC >>> "))
            if (language3 == "tr_TR"):
                settingsFileWrite3 = open("langaugeSettings.mqs", "w")
                settingsFileWrite3.write("tr_TR")
                settingsFileWrite3.close()
                ctypes.windll.user32.MessageBoxW(0, "Değişikliklerin aktif olması için programı yeniden başlatınız","Uyarı", 0)
                quit()
            if (language3 == "en_US"):
                settingsFileWrite4 = open("langaugeSettings.mqs", "w")
                settingsFileWrite4.write("en_US")
                settingsFileWrite4.close()
                ctypes.windll.user32.MessageBoxW(0, "Restart the program to save the changes.", "Warnings", 0)
                quit()
            print("")
            print("--------------------------")
            print("")
        if (userCommand != "!help" and userCommand != "!language" and userCommand != "!about" and userCommand != "!exit" and userCommand != "!github.link"):
            print("")
            print("---------------------------")
            print("İnValid Command!")
            print("---------------------------")
            print("")

