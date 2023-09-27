package main

import (
    "fmt"
    "os/user"
)

func main () {
    user, err := user.Current()
    if err != nil {
        panic(err)
    }

    fmt.Println("Hello, " + user.Username + "!")
}
