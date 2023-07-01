package arr

import (
	"errors"
	"github.com/BiangUncle/reinfL/numpy/random"
)

type FloatArr []float64

func (a *FloatArr) Len() int {
	return len(*a)
}

func (a *FloatArr) Add(obj interface{}) *FloatArr {
	switch obj.(type) {
	case int:
		return a.addInt(obj.(int))
	case float64:
		return a.addFloat64(obj.(float64))
	case IntArr:
		b := obj.(FloatArr)
		return a.addArr(&b)
	case *IntArr:
		return a.addArr(obj.(*FloatArr))
	default:
		panic(errors.New("臭傻逼"))
	}

	return a
}

func (a *FloatArr) addInt(n int) *FloatArr {
	for i := 0; i < a.Len(); i++ {
		(*a)[i] += float64(n)
	}
	return a
}

func (a *FloatArr) addFloat64(n float64) *FloatArr {
	for i := 0; i < a.Len(); i++ {
		(*a)[i] += n
	}
	return a
}

func (a *FloatArr) addArr(b *FloatArr) *FloatArr {
	if len(*a) != len(*b) {
		panic(errors.New("臭傻逼，长度都不一样"))
	}
	for i := 0; i < a.Len(); i++ {
		(*a)[i] += (*b)[i]
	}
	return a
}

func (a *FloatArr) Argmax() int {
	if len(*a) < 0 {
		panic("傻逼")
	}
	maxIndex := 0
	maxValue := (*a)[0]
	for i := 1; i < a.Len(); i++ {
		if (*a)[i] > maxValue {
			maxValue = (*a)[i]
			maxIndex = i
		}
	}
	return maxIndex
}

func (a *FloatArr) Choice() float64 {
	r := random.RandIntN(a.Len())
	return (*a)[r]
}
