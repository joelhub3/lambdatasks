# Story 3

What: Add support for unsubscribing users
Why: the existing user removal process is difficult for customer service and we should continue automating these services

Acceptance Criteria:

- Create a new lambda to process these events
- Log result for our analytics
- Log any errors or unexpected behavior

Note: The backend is adding an API for this. It should be ready by the time you start development

---

Comments:

> **From**: David Alex (Developer, EventSourcing)

We have an existing event that you can use for removing users. However, we use it
for a variety of purposes -- it's kind of a fire hose event. Here's the typescript definition:

```ts
export type CommonMessageBody = {
    date: string // ISO8601 extend -- YYYY-MM-DD'T'HH:mm:SS
    generator: string
    correlation_id: string
}

export type CreditsAdded = CommonMessageBody & {
    event_type: "credit-update"
    system_id: string
    new_credits: number
}

export type LoginEvent = CommonMessageBody & {
    event_type: "user-login"
    system_id: string
    credit_balance: number
}

export type UserUnsubscribe = CommonMessageBody & {
    event_type: "user-offboard"
    system_id: string
    reason: string
    lock_account: bool // true = immediately disable user, false = don't renew account
}

export type LogoutEvent = CommonMessageBody & {
    event_type: "user-logout"
    system_id: string
    duration_ms: number // long
    credis_used: number // int
}

```

I think you're looking for Unsubscribe?

---

> **From**: Jody Norris (Product Manager)

We have had problems with trolls recently. Make sure that troll accounts get locked out so they can't keep bothering users.

---

> **From**: Michael Gault (Senior Developer, Backend)

I just finished the new API. There are 3 fields that you need to provide:

- user_id - the user's id on the backend
- date  - when the user unsubscribed (ISO8601 -- YYYY-MM-DD) We don't need the timestamp, just the date.
- lock_out (bool) - if the user should be disabled immediately

endpoint is POST /remove-user

A successful calls return 200 with no body if the message is accepted.
A 400 is returend if we can't find the user

Also, if you need to look up the user's id, you can use the find-user API. You can find that in the docs (docs/backend.http). We'll update them with the new API soon.

Thanks!
