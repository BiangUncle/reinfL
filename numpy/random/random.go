package random

import (
	"github.com/BiangUncle/reinfL/numpy/arr"
	"math/rand"
)

// Randn 生成随机数组
func Randn(n int) *arr.FloatArr {
	r := make(arr.FloatArr, n)
	i := 0
	for i < n {
		r[i] = rand.Float64()
		i++
	}
	return &r
}

func Rand() float64 {
	return rand.Float64()
}

func RandInt() int {
	return rand.Int()
}

func RandIntN(n int) int {
	return rand.Intn(n)
}
