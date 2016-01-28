# ipython-anybar

## How install extension?

Run in ipython this command:

```%install_ext https://raw.githubusercontent.com/ermakovpetr/ipython-anybar/master/ipython_anybar.py```

## How run extension?

Run in ipython two commands:

```%load_ext ipython_anybar_ext```

and any of these commands

1. ```%ipython_anybar_connect``` default host and port = localhost, 1738
2. ```%ipython_anybar_connect [anybar port]``` default host = localhost
3. ```%ipython_anybar_connect [my mac host] [anybar port]```

## Requirements
1. Mac util: *AnyBar*

You can install it: `brew cask install anybar`

More info this: https://github.com/tonsky/AnyBar

2. Python package on computer/server with ipython: **pyanybar**

You can install it: `pip install pyanybar`

More info this: https://github.com/philipbl/pyAnyBar
