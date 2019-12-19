docker run -it --rm \
--name=mypyapp \
-e FLASK_APP=run.py \
-e FLASK_ENV=development \
-p 5000:5000 \
-v $PWD:/home/app \
mypython \
/bin/bash


# docker run -it --rm --name=rootpyapp -v $PWD:/home/myuser/app mypython /bin/bash
