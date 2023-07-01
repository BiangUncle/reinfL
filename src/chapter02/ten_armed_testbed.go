package chapter02

import (
	np "github.com/BiangUncle/reinfL/numpy"
	"github.com/BiangUncle/reinfL/numpy/arr"
	random "github.com/BiangUncle/reinfL/numpy/random"
)

type Bandit struct {
	K                int // 手臂数量
	StepSize         int
	SampleAverages   int
	Indices          []int
	Time             int
	UCBParam         interface{}
	Gradient         float64
	GradientBaseLine float64
	AverageReward    int
	TrueReward       float64
	Epsilon          float64
	Initial          *arr.FloatArr
	QTrue            *arr.FloatArr
	QEstimation      *arr.FloatArr
	ActionCount      *arr.FloatArr
	BestAction       int
}

func (b *Bandit) Init() *Bandit {
	return &Bandit{}
}

func (b *Bandit) Reset() {
	// 每个动作的真实收益
	b.QTrue = random.Randn(b.K).Add(b.TrueReward)
	// 每个动作的估计
	b.QEstimation = np.Zeros(b.K).Add(b.Initial)
	// 每个动作的选择次数
	b.ActionCount = np.Zeros(b.K)
	b.BestAction = b.QTrue.Argmax()
	b.Time = 0
}

func (b *Bandit) Act() int {
	if random.Rand() < b.Epsilon {
		return random.RandIntN(b.Initial.Len())
	}
	if b.UCBParam != nil {
		UCBEstimation := b.QEstimation.Add()
	}
}
