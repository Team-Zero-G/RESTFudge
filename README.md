# RESTFudge

A simple RESTful API for ImageFudge that allows users to upload
files to a server or local instance with ImageFudge installed, and
test its effects using the RESTful API.

## Install

    make init

## Run

    make

## Usage

Point a browser to port `5000` on your local configuration.
Upload an image file using the web interface.
The obfuscated url will be shown in the list on the right.
The part before the file extension is referred to as the `guid`.

## API

Add effects to an uploaded image

    POST: /<guid>/<imagefudge_effect>

View an image after effects have been applied

    GET: /<guid>/<imagefudge_effect>

### Supported ImageFudge Effects

*None Yet*
