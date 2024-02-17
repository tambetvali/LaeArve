package main

import "unicode"

type Code struct {
	Code string
}

type Tokens struct {
	Tokens []string
	Type   int
	Token  string
}

func (tokens *Tokens) addToken() {
	println("\"", tokens.Token, "\"")
}

func boolint(Bool bool) int {
	if Bool {
		return 1
	}
	return 0
}

func (tokens *Tokens) addLetter(letter rune) {

	var Type int

	Type = boolint(unicode.IsDigit(letter))*(2^0) +
		boolint(unicode.IsControl(letter))*(2^1) +
		boolint(unicode.IsLetter(letter))*(2^2) +
		boolint(unicode.IsNumber(letter))*(2^3) +
		boolint(unicode.IsPunct(letter))*(2^4) +
		boolint(unicode.IsMark(letter))*(2^5) +
		boolint(unicode.IsSymbol(letter))*(2^6) +
		boolint(unicode.IsSpace(letter))*(2^7)

	if tokens.Type != Type && tokens.Token != "" {
		tokens.addToken()
		tokens.Token = ""
	}

	tokens.Type = Type
	tokens.Token += string(letter)
}

func (tokens *Tokens) parse(code string) {
	runes := []rune(code)
	for _, r := range runes {
		tokens.addLetter(r)
	}
}

func (code *Code) parse() {
	var tokens Tokens
	tokens.parse(code.Code)
}

var code Code

func main() {
	code = Code{"Abc + Bcd = 7.!"}
	code.parse()
}
