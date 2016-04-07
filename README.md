# Liege Hackerspace Website

This is the repository of the Front Pages for
Liege Hackerspace (LgHS) Website. Welcome.

## How to run

The website uses the Flask Microframework to run.

1. `git clone https://github.com/LgHS/Site-V2`
1. `pip install -r requirements.txt`
1. `python3 run.py`
1. That's it!

( **Note:** Launching the app from the IDLE has been proven hazardous 
and may leave some hidden processes running in background.

Such process might still be the active one despite not preventing new ones from starting,
thus leading to situations hard to debug.)

## Dev

You can easily enable the **dev config** by setting the `LGHS_WEBSITE_CONFIG` 
to `lghs_dev_config.py`.
