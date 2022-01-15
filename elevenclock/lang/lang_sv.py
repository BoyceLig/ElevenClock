# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_1 = {
    "W": "", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "",
    "Override clock default height": "",
    "Adjust horizontal clock position": "",
    "Adjust vertical clock position": "",
    "Export log as a file": "",
    "Copy log to clipboard": "",
    "Announcements:": "",
    "Fetching latest announcement, please wait...": "",
    "Couldn't load the announcements. Please try again later": "",
    "ElevenClock's log": "",
    "Pick a color": ""
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "",
    "Enable low-cpu mode": "",
    "You might lose functionalities, like the notification counter or the dynamic background": "",
    "Clock position and size:": "",
    "Clock size preferences, position offset, clock at the left, etc.": "",
    "Reset monitor blacklisting status": "",
    "Reset": "",
    "Third party licenses": "",
    "View": "",
    "ElevenClock": "",
    "Monitor tools": "",
    "Blacklist this monitor": "",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "",
    "Ok": "",
    "More Info": "",
    "About Qt": "",
    "Success": "",
    "The monitors were unblacklisted successfully.": "",
    "Now you should see the clock everywhere": "",
    "Ok": "",
    "Blacklist Monitor": "",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "",
    "Yes": "",
    "No": "",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "",
    "Do not show the clock on secondary monitors": "",
    "Disable clock taskbar background color (make clock transparent)": "",
    "Open the welcome wizard": "",
    " (ALPHA STAGE, MAY NOT WORK)": "",
    "Welcome to ElevenClock": "",
    "Skip": "",
    "Start": "",
    "Next": "",
    "Finish": "",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "",
    "Change date and time": "",
    "Notification settings": "",
    "Updates, icon tray, language": "",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "",
    'Add the "Show Desktop" button on the left corner of every clock': '',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': '',
    "Clock's font, font size, font color and background, text alignment": "",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "",
    "Testing features and error-fixing tools": "",
    "Language pack author(s), help translating ElevenClock": "",
    "Info, report a bug, submit a feature request, donate, about": "",
    "Log, debugging information": "",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "",
    "Show the clock on the primary screen": "",
    "Use a custom font color": "",
    "Use a custom background color": "",
    "Align the clock text to the center": "",
    "Select custom color": "",
    "Hide the clock when a program occupies all screens": "",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Använd en anpassad font",
    "Use a custom font size": "Använd en anpassad font storlek",
    "Enable hide when multi-monitor fullscreen apps are running": "Aktivera dölj när helskärmsappar med flera skärmar körs",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> måste vara aktiverat för att ändra denna inställning",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> måste inaktiveras för att ändra den här inställningen",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Den här funktionen har inaktiverats eftersom den borde fungera som standard. Om den inte är det, rapportera ett fel)",
    "ElevenClock's language": "ElevenClocks språk"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Om Qt6 (PySide6)",
    "About": "Om",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternativ icke-SSL-uppdateringsserver (Detta kan hjälpa till med SSL-fel)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Fixar och andra experimentella funktioner: (Använd ENDAST om något inte fungerar)",
    "Show week number on the clock": "Visa veckonummer på klockan"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Dölj klockan när RDP Client eller Citrix Workspace körs",
    "Clock Appearance:": "Klockans utseende",
    "Force the clock to have black text": "Tvinga klockan att ha svart text",
    " - It is required that the Dark Text checkbox is disabled": " - Det krävs att kryssrutan Mörk text är inaktiverad",
    "Debbugging information:": "Debugging information",
    "Open ElevenClock's log": "Öppna ElevenClocks logg",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Visa klockan på den primära skärmen (Användbart om klockan är inställd till vänster)",
    "Show weekday on the clock"  :"Visa veckodag på klockan",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock Inställningar", # Also settings title
    "Reload Clocks"             :"Ladda om klockor",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Starta om ElevenClock",
    "Hide ElevenClock"          :"Göm ElevenClock",
    "Quit ElevenClock"          :"Avsluta ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Allmänna Inställningar:",
    "Automatically check for updates"                                                   :"Sök automatiskt efter uppdateringar",
    "Automatically install available updates"                                           :"Installera tillgängliga uppdateringar automatiskt",
    "Enable really silent updates"                                                      :"Aktivera riktigt tysta uppdateringar",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Kringgå uppdateringsleverantörens äkthetskontroll (REKOMMENDERAS INTE, PÅ DIN EGEN RISK)",
    "Show ElevenClock on system tray"                                                   :"Visa ElevenClock i systemfältet",
    "Alternative clock alignment (may not work)"                                        :"Alternativ klockjustering (fungerar kanske inte)",
    "Change startup behaviour"                                                          :"Ändra startbeteende",
    "Change"                                                                            :"Förändra",
    "<b>Update to the latest version!</b>"                                              :"<b>Uppdatera till den senaste versionen!</b>",
    "Install update"                                                                    :"Installera uppdatering",
    
    #Clock settings
    "Clock Settings:"                                              :"Klockinställningar:",
    "Hide the clock in fullscreen mode"                            :"Dölj klockan i helskärmsläge",
    "Hide the clock when RDP client is active"                     :"Dölj klockan när RDP-klienten är aktiv",
    "Force the clock to be at the bottom of the screen"            :"Tvinga klockan att vara längst ner på skärmen",
    "Show the clock when the taskbar is set to hide automatically" :"Visa klockan när aktivitetsfältet är inställt på att döljas automatiskt",
    "Fix the hyphen/dash showing over the month"                   :"Åtgärda bindestrecket/strecket som visas under månaden",
    "Force the clock to have white text"                           :"Tvinga klockan att ha vit text",
    "Show the clock at the left of the screen"                     :"Visa klockan till vänster på skärmen",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Inställningar för datum och tid:",
    "Show seconds on the clock"                         :"Visa sekunder på klockan",
    "Show date on the clock"                            :"Visa datum på klockan",
    "Show time on the clock"                            :"Visa tid på klockan",
    "Change date and time format (Regional settings)"   :"Ändra datum och tidsformat (regionala inställningar)",
    "Regional settings"                                 :"Regionala inställningar",
    
    #About the language pack
    "About the language pack:"                  :"Om språkpaketet:",
    "Translated to English by martinet101"      :"Översatt till Svenska av Noffe", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Översätt ElevenClock till ditt språk",
    "Get started"                               :"Komma igång",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Om ElevenClock version {0}:",
    "View ElevenClock's homepage"               :"Visa ElevenClocks hemsida",
    "Open"                                      :"Öppna",
    "Report an issue/request a feature"         :"Rapportera ett problem/begär en funktion",
    "Report"                                    :"Rapportera",
    "Support the dev: Give me a coffee☕"       :"Stöd utvecklaren: Ge mig en kaffe☕",
    "Open page"                                 :"Öppna sida",
    "Icons by Icons8"                           :"Ikoner av Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Webbsida",
    "Close settings"                            :"Stäng inställningar",
    "Close"                                     :"Stäng",
}

lang = lang2_3
