package main


import (
	"fmt"
	"strconv"
	"math"
	"os"
	"os/exec"
)


type quartInt int

const capacity int = 4


func main() {
	userInterface()
}

func addition(a, b quartInt) quartInt {
	sign := ""
	if x := int(a) * int(b); x < 0 {
		if a < b {
			a, b = b, a * quartInt(-1)
		} else {
			b *= quartInt(-1)
		}
		return subtraction(a, b)
	} else {
		switch {
		case int(a) < 0 && int(b) < 0:
			sign = "-"
		case int(a) == 0:
			return b
		case int(b) == 0:
			return a
		}
	}

	strA, strB := strconv.Itoa(int(a)), strconv.Itoa(int(b))
	lenA, lenB := len(strA), len(strB)
	var length int
	var head string
	var tempStr []rune

	if lenA < lenB {
		length = lenA
		tempStr = []rune(strB)
		head = string(tempStr[:lenB - length])
		strB = string(tempStr[lenB - length:])
	} else {
		length = lenB
		tempStr = []rune(strA)
		head = string(tempStr[:lenA - length])
		strA = string(tempStr[lenA - length:])
	}

	var add, intA, intB int
	overflow := 0
	result := ""


	for i := length - 1; i >= 0; i-- {
		intA, _ = strconv.Atoi(string(strA[i]))
		intB, _ = strconv.Atoi(string(strB[i]))
		add = intA + intB + overflow
		overflow = 0
		if add >= capacity {
			overflow = add / capacity
			add %= capacity
		}
		result = strconv.Itoa(add) + result

		if i == 0 {
			switch {
			case lenA == lenB:
				result = sign + strconv.Itoa(overflow) + result
			default:
				tempStr = []rune(head)
				tempI, _ := strconv.Atoi(string(rune(head[len(head) - 1])))
				result = sign + string(tempStr[:len(head) - 1]) + strconv.Itoa(tempI + overflow) + result
			}
		}
	}

	res, _ := strconv.Atoi(result)
	return quartInt(res)
}

func subtraction(a, b quartInt) quartInt {
	sign := ""
	if x := int(a) * int(b); x < 0 {
		b *= quartInt(-1)
		return addition(a, b)
	} else {
		switch {
		case int(a) < 0 && int(b) < 0:
			sign = "-"
			if math.Abs(float64(a)) < math.Abs(float64(b)) {
				a, b = b * quartInt(-1), a * quartInt(-1)
				return subtraction(a, b)
			}
		case int(a) < int(b):
			a, b = b * quartInt(-1), a * quartInt(-1)
			return subtraction(a, b)
		case int(a) == 0:
			return b
		case int(b) == 0:
			return a
		}
	}

	strA, strB := strconv.Itoa(int(a)), strconv.Itoa(int(b))
	lenA, lenB := len(strA), len(strB)
	var length int
	var head string
	var tempStr []rune

	if lenA < lenB {
		length = lenA
		tempStr = []rune(strB)
		head = string(tempStr[:lenB - length])
		strB = string(tempStr[lenB - length:])
	} else {
		length = lenB
		tempStr = []rune(strA)
		head = string(tempStr[:lenA - length])
		strA = string(tempStr[lenA - length:])
	}

	var sub, intA, intB int
	overflow := 0
	result := ""

	for i := length - 1; i >= 0; i-- {
		intA, _ = strconv.Atoi(string(strA[i]))
		intB, _ = strconv.Atoi(string(strB[i]))
		intA -= overflow
		overflow = 0
		if intA < intB {
			sub = intA - intB + capacity
			overflow = 1
		} else {
			sub = intA - intB
		}
		result = strconv.Itoa(sub) + result

		if i == 0 {
			switch {
			case lenA == lenB:
				result = sign + result
			default:
				tempStr = []rune(head)
				tempI, _ := strconv.Atoi(string(rune(head[len(head) - 1])))
				result = sign + string(tempStr[:len(head) - 1]) + strconv.Itoa(tempI - overflow) + result
			}
		}
	}

	res, _ := strconv.Atoi(result)
	return quartInt(res)
}

func toDecimal(number quartInt) (result int){
	strNumber := strconv.Itoa(int(number))

	for i, j := 0, len(strNumber)-1; i < len(strNumber); i, j = i+1, j-1 {
		value, _ := strconv.Atoi(string(strNumber[j]))
		result += value * int(math.Pow(float64(capacity), float64(i)))
	}

	if int(number) < 0 {
		result *= -1
	}

	return result
}

func fromDecimal(number int) quartInt{
	modulo := 0
	strResult := ""
	sign := ""

	if number < 0 {
		sign = "-"
		number *= -1
	}

	for {
		modulo = number % capacity
		number /= capacity
		strResult = strconv.Itoa(modulo) + strResult
		if number == 0 {
			break
		}
	}

	result, _ := strconv.Atoi(sign + strResult)

	return quartInt(result)
}

func userInterface() {
	v := 5
	for v!= 0 {
		v = 0
		clrscr()
		fmt.Println("Welcome")
		fmt.Println("Input number of operation:")
		fmt.Println("[1] Decimal to quart")
		fmt.Println("[2] Quart to decimal")
		fmt.Println("[3] Addition")
		fmt.Println("[4] Subtraction")
		fmt.Println("[0] Quit")
		fmt.Scanf("%d", &v)

		switch v {
		default:
		case 1:
			var a int
			clrscr()
			fmt.Println("Input number")
			fmt.Scanf("%d", &a)
			fmt.Println(fromDecimal(a))
			fmt.Scanln()
		case 2:
			var a quartInt
			clrscr()
			fmt.Println("Input number")
			fmt.Scanf("%d", &a)
			fmt.Println(toDecimal(a))
			fmt.Scanln()
		case 3:
			var a, b quartInt
			clrscr()
			fmt.Println("Input numbers")
			fmt.Scanf("%d %d", &a, &b)
			fmt.Println(addition(a, b))
			fmt.Scanln()
		case 4:
			var a, b quartInt
			clrscr()
			fmt.Println("Input numbers")
			fmt.Scanf("%d %d", &a, &b)
			fmt.Println(subtraction(a, b))
			fmt.Scanln()
		}
		clrscr()
	}

}

func clrscr() {
	c := exec.Command("clear")
	c.Stdout = os.Stdout
	c.Run()
}
