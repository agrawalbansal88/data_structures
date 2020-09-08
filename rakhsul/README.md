# Gofactor - A Refactoring Challenge

This tiny REST API was written hastily as a proof-of-concept. It mostly does what it's supposed to do, but it's buggy and not very maintainable.

Time for some major refactoring!

## Requirements

Please make the following changes:

1. The code should be split into at least 3 separate layers that demonstrate clear separation of concerns.

   HINT: Take your _inspiration_ from the [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) pattern.

   HINT: Showcase proper use of dependency injection and Go interfaces.

1. Use [gorilla/mux](https://github.com/gorilla/mux) to replace _http.ServeMux_ where needed.

   **NOTE: Unfortunately, you're _not allowed_ to switch over to a web framework like Echo or Gin :-(**

1. All logging output _MUST_ be JSON strings. Use the [zap](https://github.com/uber-go/zap) package. You _CAN_ decide where and what to log.

1. All errors _MUST_ be handled and logged properly and produce sensible error messages. Use the [github.com/pkg/errors](https://github.com/pkg/errors) package.

1. Fix the **POST** `/user` route so that it _validates_ the inbound JSON payload to be:

   ```js
   {
        "email": string    // Should be a valid email address
        "name":  string    // Should be at least 2 chars long
        "password": string // Should be at least 8 chars long
   }
   ```

   Use [validator.v10](https://gopkg.in/go-playground/validator.v10) to handle struct validation. _DO NOT_ create any custom validators (use only built-in validators).

   Make sure the password is stored correctly, i.e. following best-practices. Use the [bcrypt](https://godoc.org/golang.org/x/crypto/bcrypt) package.

   Return the newly created user as JSON.

1. Change **GET** `/user` route to **GET** `/user/{id}` and receive the `id` as a route var.

   Return user as JSON.

1. Change **PATCH** `/user` route to **PATCH** `/user/{id}` and receive the `id` as a route var.

   Currently all fields are updated at the same time - which is a serious bug!

   Make sure fields can be updated independently and only when passing a valid value (ignore zero values).

   Return updated user as JSON.

1. The `CREATE TABLE` DDL statement is "lacking" in several ways. See if you can find ways to improve it.

1. API keys and database credentials (username & password) should _NOT_ be hard coded in the app. Use _env vars_ instead and create some kind of config struct to hold these values.

   - Do _NOT_ create an external config file (e.g. config.json).
   - Do _NOT_ make the query string part of the DSN string configurable, i.e. leave the `?timeout=90s&charset=utf8mb4&collation=utf8mb4_unicode_ci&parseTime=true` bit hard coded.

1. All routes _MUST_ return only JSON.

1. Write _one end-to-end test suite_ that tests the routes **POST** `/user`, **GET** `/user` and **PATCH** `/user` _within the same test_.

   Use the [testify](https://github.com/stretchr/testify) package.

1. Add a `docker-compose.yml` file that defines our dependency on MySQL.

1. Dockerize this project. Add a `Dockerfile` that builds our back-end inside a Docker container using `Golang v1.14.6` (this exact version of Golang) and ensure that the resulting Docker image is _as small as possible_.

1. The `latestReviews` route handler has some problems:

   - It fetches the latest movie reviews from NY Times on every call, even though movie reviews aren't updated that often.
   - It collects the response as a slice of strings, which works, but looks rather messy.

   Refactor as follows:

   1. The code _MUST_ call the NY Times API _1 time / hour_ in the background and cache the result.

   1. We _MUST_ be able to call the `latestReviews` handler _hundreds of times per sec_ yet _NEVER_ end up calling the NY Times API more than _1 time / hour_.

   1. Returning pretty-printed JSON isn't really necessary. We can simply return whatever we get from the NY Times API _without any parsing / unmarshalling_.

      HINT: Given this, you should be able to simplify the code significantly!

1. Add comments to your code to make it more readable!

1. **IMPORTANT: Keep your implementation to as few lines of code as possible.**

   The original program is 207 LOC, so you wouldn't be helping matters by coming up with a solution that's 7-10x bigger than that!

## Important Notes

1. You can spend as much time as you want doing this exercise, but you should submit your final PR **within 7 days of getting access to this repository**.

   NOTE: You'll only be judged on the final PR, not the number of commits you have nor the total time spent on the exercise.

1. Besides the packages explicitly mentioned / recommended above, you're _ONLY_ allowed to use the Go standard library.

1. You're free to restructure and refactor the code in any way you see fit. Go nuts!

1. Don't worry too much about finishing everything to the fullest extent possible. The purpose of this exercise is to have candidates demonstrate a firm grasp of Go fundamentals and knowledge of the overall Go ecosystem. We expect our Senior Engineers to be able to guide others on how to write clean, maintainable Go code.

1. Submit your work as a PR. Be sure to:

   - **Create a separate feature branch and create a PR from it** so that we can perform a standard code review on Github.

1. **Write clean code.** We value _good naming, comments, structure and overall readability_ of your code above all else.

1. **Do _NOT_ over-engineer things unnecessarily.** Keeping things simple, showing restraint and making mature choices will be crucial.

Happy Hacking!
