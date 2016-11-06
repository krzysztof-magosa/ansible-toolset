setup() {
    echo "some-password" > ansible-vault-password
    export ANSIBLE_VAULT_PASSWORD_FILE=ansible-vault-password
}

@test "create, plain text" {
    cp template.yml test.yml
    ats-vault create test.yml
    run grep -q '$ANSIBLE_VAULT' test.yml

    [ "$status" -eq 0 ]
}

@test "create, already encrypted" {
    cp template.yml test.yml
    ats-vault create test.yml
    run ats-vault create test.yml

    [ "$output" = "Provided file is already encrypted." ]
}

@test "grep" {
    cp template.yml test.yml
    ats-vault create test.yml
    run ats-vault grep admin2

    [ "$output" = "test.yml:2:password2: admin2" ]
}

@test "rgrep" {
    cp template.yml test.yml
    ats-vault create test.yml
    run ats-vault rgrep 'admin\d+'

    [ "$(echo "$output" | head -n1)" = "test.yml:1:password1: admin1" ]
    [ "$(echo "$output" | tail -n1)" = "test.yml:2:password2: admin2" ]
}

@test "open" {
    cp template.yml test.yml
    ats-vault create test.yml
    ats-vault open

    [ "$(cat test.yml)" = "$(cat template.yml)" ]
}

# close
