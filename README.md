`ech` is a tool to manage AWS EC2 instances. It can 

- Start/stop instances in multiple regions and users.
- Add the instance to you SSH profile. 

## Install

- Install `aws-cli` from [here](https://aws.amazon.com/cli/).
- `pip install ech`

## How to use

Suppose I have a instance with id `i-01234567` in `us-west-2` under default profile, and a instance with id `i-76543210` in `us-east-1` under profile `tom`. To manage those

- Run `aws configure` to add default profile if you haven't done so, and go to `~/.aws/credentials` to add profile for `tom`. 

- Create `awsh.toml` in your home directory:

  ```toml
  [servers]
  my-server = {id = "i-01234567", region="us-west-2"}
  another-server = {id = "i-76543210", region="us-east-1"}
  ```

  Now you created two server alias `my-server` `another-server`.

Now suppose you want to start your work on `my-server`.

#### Start your instance

```sh
ech start my-server
```

#### Connect to your instance

First, add this server to your SSH profile.

```sh
ech bind my-server
```

The next step is straightforward:

```sh
ssh my-server
```

**Tip:** You can directly access this instance in your VSCode by selecting `my-server` installing SSH plugin and remote explorer. 

#### Stop your instance

```sh
ech stop my-server
```

That's it. 

*I am using this tool quite often in my personal study/work, but this tool may/should still have bugs. If so please submit an issue. Thanks!*