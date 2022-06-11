# Inkscape Scripts

* Utility scripts to make creating designs in [Inkscape](https://inkscape.org/) easier.
* The scripts are executed with the extension [Simple Inkscape Scripting](https://github.com/spakin/SimpInkScr).
* See the [Simple Inkscape Scripting Wiki](https://github.com/spakin/SimpInkScr/wiki) on how to use the scripting API.


## Installing *Simple Inkscape Scripting*

1. Install *Inkscape v1.1.2* via https://inkscape.org/release/1.1.2/windows/64-bit/.  
   > **IMPORTANT!** Make sure to use v1.1.2, I tried using the extension with v1.2 which didn't work.
2. Downloaded the [lastest release](https://github.com/spakin/SimpInkScr/releases/latest) of *Simple Inkscape Scripting*.
3. Unzip the archive to get the folder `simple_inkscape_scripting`.
4. Open Inkscape, go to `Extensions --> Manage Extensions...`. This opens the *Extensions Manager*. 
5. Click on tab "Install Packages", then click on the folder icon in the command bar. This opens a file explorer.
6. Navigate to the unzipped `simple_inkscape_scripting` folder, select the folder and click "Open".
7. Depending on your Inkscape configuration, this installs the plugin locally to your user, e.g. `C:\Users\Joe\AppData\Roaming\inkscape\extensions\org.pakin.output.simple_inkscape_scripting\simple_inkscape_scripting` (on Windows).  
8. Alternatively, you can simply skip steps 5 to 7 and copy the folder `simple_inkscape_scripting` directly to `C:\Program Files\Inkscape\share\inkscape\extensions` (on Windows).
9. Restart Inkscape.
10. Open a new document via "New Document".
11. Start the extension via `Menubar --> Extensions --> Render --> Simple Inkscape Scripting...`
12. Insert a [simple example script](https://github.com/spakin/SimpInkScr/blob/master/examples/ellipses.py) into the field "Python code":
    ```py
    for i in range(10, 0, -1):
        ellipse((width/2, height/2), (i*30, i*20 + 10),
                fill='#0000%02x' % (255 - 255*i//10), stroke='white')
    ```
13. Click on "Apply".
14. A group of blue ellipsis should be rendered on screen.  
    Congratz! You just ran your first Inkscape script!


## Checking if *Simple Inkscape Scripting* is installed 

1. Start Inkscape.  
   > **IMPORTANT!** Make sure to use v1.1.2, I tried using the *Extension Manager* with v1.2 and I couldn't display details about orphan packages.
2. Go to `Menubar --> Extensions --> Render`. There should be a command "Simple Inkscape Scripting...".
3. Alternatively, check via the *Extensions Manager*: 
   * go to `Extensions --> Manage Extensions...`. This opens the *Extensions Manager*. 
   * In the *Extensions Manager*, click on "Active Packages" then on "Orphan Extensions". 
   * Click on the button "Details", this opens another dialogue. 
   * Click on "Lost-And-Found" in the tree view to expand it, there you should see `\org.pakin.output.simple_inkscape_scripting\simple_inkscape_scripting\simple_inkscape_scripting.inx` (or something similar).
