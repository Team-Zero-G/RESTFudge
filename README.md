[![Build Status](https://travis-ci.org/konstantinfarrell/RESTFudge.svg?branch=master)](https://travis-ci.org/konstantinfarrell/RESTFudge)

# RESTFudge

A simple RESTful API for ImageFudge that allows users to upload
files to a server or local instance with ImageFudge installed, and
test its effects using the RESTful API.

## Install

    make init

## Usage

For a local configuration, run

    make

Then point a browser to port `5000`.
Upload an image file using the web interface.
The obfuscated url will be shown in the list on the right.
The part before the file extension is referred to as the `slug`.

## API

View an uploaded image

    GET: /<slug>

Add effects to an uploaded image

    POST: /<slug>/<imagefudge_effect>

View an image after effects have been applied

    GET: /<slug>/<imagefudge_effect>

### Supported ImageFudge Effects

    get_relative_arcs
    fuzzy
