# Django-Stripe-Payment APIs

The project contains an implementation of integration between Stripe and Django.

## Project Setup

Cloning the project into your local machine

```bash
git clone https://github.com/gshubham82/Django-Stripe-Payment.git
```

## Stripe Configuration

Before running the docker-compose build command, create a sandbox account on Stripe to get access key and secret key by clicking on 
[Stripe Register](https://dashboard.stripe.com/register)

Once you get the access key and secret key, create an environmental file in the working directory.
``` 
mkdir .env 
```
```
STRIPE_PUBLISHABLE_KEY= your_stripe_publishable_key

STRIPE_SECRET_KEY= your_stripe_secret_key
```
Once the environmental file is created edit the file and add the keys and save the file.

## Project Execution

Once the above steps are completed, it's time to run the Docker.

```
docker-compose build

docker-compose up
```
Once the docker is running, we can test the APIs.

## APIs

Postman Collection demonstrating how to use the Django-REST API.
More information about the API can be found in the [API Documentation](https://documenter.getpostman.com/view/12323262/UVeCQTxo).

To use the latest published version, click the following button to import the Django-Stripe-Payment API as a collection:

[![Run in Postman](https://s3.amazonaws.com/postman-static/run-button.png)](https://app.getpostman.com/run-collection/219575449c5886aae16f)

You can also download the collection file from this repository, then import directly into Postman.

### Prerequisites

- *Postman* The collection is for use by the Postman app. Postman is a utility that allows you to quickly test and use REST APIs. More information can be found at [getpostman.com](https://www.getpostman.com/).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Reference
[Stripe API docs](https://stripe.com/docs/api)
