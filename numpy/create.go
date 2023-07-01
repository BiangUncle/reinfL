package numpy

import "github.com/BiangUncle/reinfL/numpy/arr"

func Zeros(n int) *arr.FloatArr {
	r := make(arr.FloatArr, n)
	for i := 0; i < n; i++ {
		r[i] = 0.0
	}
	return &r
}
