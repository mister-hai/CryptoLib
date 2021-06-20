Library for performing statistical / crypto operations

Work in progress, This is for me to learn.

I am thinking of making a flask interface with a 
jupyterlabs notebook in it for plotting metrics and the like.

Project structure is as thus (for the moment):

    app.py   ---> main file for running the project
    src/
        __init__.py
        util/
            crypto/
                diffiehellmangeneratekey.py
                mersennetwist.py
            stats/
                entropy.py
                probabilitymassfunciton.py
                standarddeviation.py
            Utils.py
        tools/
            curve25519.py
            entropypool.py
            xorshift.py
        primitives/
            distributedpointfunciton.py
            ellipticalcurve.py
            onewaycompression.py
            vonneumanextractor.py

