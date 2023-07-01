package arr

import "errors"

type IntArr []int

func (a *IntArr) Len() int {
	return len(*a)
}

func (a *IntArr) Add(obj interface{}) *IntArr {
	switch obj.(type) {
	case int:
		return a.addInt(obj.(int))
	case IntArr:
		b := obj.(IntArr)
		return a.addArr(&b)
	case *IntArr:
		return a.addArr(obj.(*IntArr))
	default:
		panic(errors.New("臭傻逼"))
	}

	return a
}

func (a *IntArr) addInt(n int) *IntArr {
	for i := 0; i < a.Len(); i++ {
		(*a)[i] += n
	}
	return a
}

func (a *IntArr) addArr(b *IntArr) *IntArr {
	if len(*a) != len(*b) {
		panic(errors.New("臭傻逼，长度都不一样"))
	}
	for i := 0; i < a.Len(); i++ {
		(*a)[i] += (*b)[i]
	}
	return a
}
