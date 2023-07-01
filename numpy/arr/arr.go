package arr

type ArrInterface interface {
	Len() int
	Get(int) int
	Set(int, interface{})
}

type Value struct {
}

type ArrIntf struct {
	l []Value
}
