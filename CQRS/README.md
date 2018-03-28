## Command Query Responsibility Segregation (CQRS) Notes

Why?
- Seperate the Read Model and Write Model
- this design gives us a "free" audit log of events that can be replayed to construct original state, think react-redux but instead of client application state
we're dealing with business application state.


### Examples

#### Bank Account

We will build a bank account with 3 functions:

`open_account/2`

`deposit/2`

`withdraw/2`

```
# intial empty account state
account = %BankAccount{}

# open the account returns an account opened event
account_opened = BankAccount.open_account(account, %BankAccount.Commands.OpenAccount{
    account_number: "ACC123",
    initial_balance: 100.00,
})

# mutate the bank account state by applying the opened event
account = BankAccount.apply(account, account_opened)

```

Intuition: We can think of the final state as an accumulation of events, or the aggregate view. We will "reduce" down to the final state,
and apply whatever the next event is to final state, to reach the next state.

```
state = ExampleAggregate.apply(state, some_event)

# or view as
state =
    state
    |> ExampleAggregate.apply(event_1)
    |> ExampleAggregate.apply(event_2)
    |> ExampleAggregate.apply(event_3)

# or more concretely:

my_bank_account =
    %BankAccount{}
    |> BankAccount.open_account(%BankAccount.Commands.OpenAccount{
        account_number: "ACC123",
        initial_balance: 100,
    })
    |> BankAccount.deposit(%BankAccount.Commands.Deposit{
        amount: 100
    })
    |> BankAccount.withdraw(%BankAccount.Commands.Withdraw{
        amount: 75
    })


```


#### Readings
[Martin Fowler on CQRS](https://martinfowler.com/bliki/CQRS.html)
[Building a CQRS/ES Web Application in Elixir Using Phoenix](https://10consulting.com/2017/01/04/building-a-cqrs-web-application-in-elixir-using-phoenix/)

[Microsoft Explanation](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs)
[Reddit Discussion](https://www.reddit.com/r/programming/comments/3l0hp1/achieving_consistency_in_cqrs_with_linear_event/)
