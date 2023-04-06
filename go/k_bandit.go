package main

import "math/rand"

func Init(k int) ([]float64, []float64) {
	Q := make([]float64, k)
	N := make([]float64, k)
	return Q, N
}

func selectAction(Q []float64, epsilon float64) int {
	action := 0
	randFloat := rand.Float64()
	// a random action
	if randFloat < epsilon {
		action = rand.Intn(len(Q))
		return action
	}
	// argmax
	maxValue := Q[action]
	for i, q := range Q {
		if q > maxValue {
			action = i
		}
	}
	return action
}

func bandit(a int) float64 {
	return 1.0
}

func run(times int, epsilon float64, Q, N []float64) {
	i := 0
	for {
		a := selectAction(Q, epsilon)
		R := bandit(a)
		N[a] = N[a] + 1
		Q[a] = Q[a] + (1/N[a])*(R-Q[a])
		i++
		if i >= times {
			break
		}
	}
}
