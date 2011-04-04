FlexPilot Setup Example
=======================

This assumes that you have python installed and are using Firefox 3.6.

Step By Step Setup Instructions
-------------------------------

1. Make a folder on your desktop called 'flexpilot'.
2. Go and download the Adobe Fles SDK (version 3.5) from [here]("http://opensource.adobe.com/wiki/display/flexsdk/download?build=3.5.0.12683&pkgtype=1&release=3 "). Make sure this is in the flexpilot folder or add it to your path.
3. From this repo download index.html and new_test.mxml into the flexpilot folder as well.
4. Compile the flexpilot.mxml with mxmlc from the Adobe SDK, like so:
    flex_sdk/bin/mxmlc new_test.mxml
5. Start a web server with:
    python -m SimpleHTTPServer
6. Go to localhost:8000 and confirm that everything is present and working.
7. Go to the FlexPilot repo [here] ("https://github.com/mde/flex-pilot") in the downloads section download FlexPilot-3-stable.swf into the flexpilot folder.
8. Also, download the FPBootstrap.zip, extract it and move the lib folder into the flexpilot folder.
9. Now open up flexpilot.mxml and modify the application tag so that it will call the FPBootstrap code when the application is loaded, like this:
    <mx:Application xmlns:mx="http://www.adobe.com/2006/mxml" layout="absolute" applicationComplete="init();">
10. Within the script tags import FPBootstrap and define the init() function:
    import org.flex_pilot.FPBootstrap

    private function init():void {
      FPBootstrap.flex_pilotLibPath = 'FlexPilot-3-stable.swf'
      FPBootstrap.init(stage)
    }
11. Now recomplile flexpilot.mxml, specifying that the compiler should look in the lib directory for source:
    flex_sdk/bin/mxmlc -source-path=. -source-path+=lib flexpilot.mxml
12. Resart the python server and check to see that everything looks OK, and there are no 404s. You should see FlexPilot-3-stable.swf being served by the server. If its a 404 check your paths.
13. To make sure everything is set up correctly go into Firebug and run:
    document.getElementsByName[0].fp_click
This should output 'function' which means that everything is set up and we can start testing. If it returns undefined then something went wrong.
14. Go to the [SeleniumHQ] ("http://seleniumhq.org/downloads") page and download the Selenium IDE v1.0.10, as well as Selenium Server v2.0b3.
15. Now go to the [FlexPilot X] ("http://github.com/admc/flex-pilot-x") repo and download plugin v0.83 as well as the Python client driver which is in the client folder under Python.
16. Put the selenium.py file you just downloaded into your flexpilot folder.
