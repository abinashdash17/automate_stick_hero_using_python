# automate_stick_hero_using_python
Pre-requisites:
on mobile
  install stick hero from playstore
on computer
  1.install adb
    -in linux android-tools-adb
    -in windows install 
    -in mac : ?
  2.install python3 and required python packages (pillow,numpy,pure-python-adb)
  3.install scrcpy(optional - to mirror android screen to computer)
  -in linux install the package from software repo
  -for other os check the https://github.com/Genymobile/scrcpy

steps
  1.open the game
  2.touch on start
  3.run the program stick_hero.py on computer
  4.let the the program play the game
  5. hit ctrl+C to kill the program
caution:
this program does not check whether the game is open. It sends touch events to the android screen as per algorithm wrtitten in the program. If the game is not open,
it may interfer with other open apps. To check whether the program is sending touch events correctly, enable touch event log from developer options.
