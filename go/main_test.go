package main

import (
	"fmt"
	"math/rand"
	"sort"
	"strconv"
	"testing"
	"time"
	//"unsafe"
)

const (
	numItems = 100
)
const fixString = "testStr"

type myArr struct {
	key string
	val int
}
type myIntArr struct {
	key uint32
	val string
}

func compare(i, j int) bool { return sortedArr[i].key < sortedArr[j].key }

func compareInt(i, j int) bool { return sortedIntArr[i].key < sortedIntArr[j].key }

var strToIntMap map[string]uint32
var intToStrMap map[uint32]string
var strArr []myArr
var intArr []myIntArr
var sortedArr []myArr
var sortedIntArr []myIntArr

func fillMapSlice() (string, uint32) {
	rand.Seed(time.Now().UnixNano())
	queryI := rand.Int31n(numItems)

	var query string

	strToIntMap = make(map[string]uint32, numItems)
	strArr = make([]myArr, numItems)
	sortedArr = make([]myArr, numItems)
	intToStrMap = make(map[uint32]string, numItems)
	intArr = make([]myIntArr, numItems)
	sortedIntArr = make([]myIntArr, numItems)
	for i := 0; i < numItems; i++ {
		k := fixString + strconv.Itoa(i)
		strToIntMap[k] = uint32(i)
		strArr[i] = myArr{key: k, val: i}
		sortedArr[i] = myArr{key: k, val: i}
		if i == int(queryI) {
			query = k
		}

		intToStrMap[uint32(i)] = k
		intArr[i] = myIntArr{key: uint32(i), val: k}
		sortedIntArr[i] = myIntArr{key: uint32(i), val: k}
	}
	//fmt.Println(strToIntMap)
	//fmt.Println(strArr)
	sort.SliceStable(sortedArr, compare)
	//fmt.Println(sortedArr)
	//fmt.Println("Search Key", query)
	return query, uint32(queryI)
}

func BenchmarkMap(b *testing.B) {
	var found bool
	qStr, _ := fillMapSlice()
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		if _, ok := strToIntMap[qStr]; ok {
			found = true
		}
		if !found {
			b.Fail()
		}
	}

}

func BenchmarkSlice(b *testing.B) {
	var found bool
	qStr, _ := fillMapSlice()
	b.ResetTimer()

	for n := 0; n < b.N; n++ {
		for j := 0; j < numItems; j++ {
			if strArr[j].key == qStr {
				found = true
			}
		}
		if !found {
			b.Fail()
		}
	}

}

func BenchmarkSortedSlice(b *testing.B) {
	var found bool
	qStr, _ := fillMapSlice()
	b.ResetTimer()

	for n := 0; n < b.N; n++ {
		index := sort.Search(numItems, func(i int) bool {
			return sortedArr[i].key >= qStr
		})
		if index < len(sortedArr) && sortedArr[index].key == qStr {
			found = true
		}
		if !found {
			fmt.Println("Not found in sorted Slice", qStr)
			b.Fail()
		}
	}

}
func BenchmarkCopyMap(b *testing.B) {
	fillMapSlice()
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		smVar := make(map[string]uint32, len(strToIntMap))
		if len(strToIntMap) > 0 {
			for key, item := range strToIntMap {
				smVar[key] = item
			}
		}
	}
}

func BenchmarkCopySlice(b *testing.B) {
	fillMapSlice()
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		smVar := make([]myArr, len(strArr))
		if len(strArr) > 0 {
			for indx, item := range strArr {
				smVar[indx] = item
			}
		}
	}
}

func BenchmarkInsertSortedSlice(b *testing.B) {
	fillMapSlice()
	b.ResetTimer()
	val := 2000
	e := fixString + strconv.Itoa(val)
	arrEl := myArr{key: e, val: val}
	for n := 0; n < b.N; n++ {

		sortedArr = append(sortedArr, arrEl)
		sort.SliceStable(sortedArr, compare)

	}
	//b.ResetTimer()
	//fmt.Println("Length of slice:", len(sortedArr))

}

func BenchmarkInsertMap(b *testing.B) {
	fillMapSlice()
	b.ResetTimer()
	val := 2000
	e := fixString + strconv.Itoa(val)
	for n := 0; n < b.N; n++ {
		strToIntMap[e] = uint32(val)
	}

}

//INT Key Functions

func BenchmarkIntMap(b *testing.B) {
	var found bool
	_, q := fillMapSlice()
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		if _, ok := intToStrMap[q]; ok {
			found = true
		}
		if !found {
			b.Fail()
		}
	}

}

func BenchmarkIntSlice(b *testing.B) {
	var found bool
	_, q := fillMapSlice()
	b.ResetTimer()

	for n := 0; n < b.N; n++ {
		for j := 0; j < numItems; j++ {
			if intArr[j].key == q {
				found = true
			}
		}
		if !found {
			b.Fail()
		}
	}

}

func BenchmarkSortedIntSlice(b *testing.B) {
	var found bool
	_, q := fillMapSlice()
	b.ResetTimer()

	for n := 0; n < b.N; n++ {
		index := sort.Search(numItems, func(i int) bool {
			return sortedIntArr[i].key >= q
		})
		if index < len(sortedArr) && sortedIntArr[index].key == q {
			found = true
		}
		if !found {
			fmt.Println("Not found in sorted Slice", q)
			b.Fail()
		}
	}

}

func BenchmarkCopyIntMap(b *testing.B) {
	fillMapSlice()
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		smVar := make(map[uint32]string, len(intToStrMap))
		if len(intToStrMap) > 0 {
			for key, item := range intToStrMap {
				smVar[key] = item
			}
		}
	}
}

func BenchmarkCopyIntSlice(b *testing.B) {
	fillMapSlice()
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		smVar := make([]myIntArr, len(intArr))
		if len(intArr) > 0 {
			for indx, item := range intArr {
				smVar[indx] = item
			}
		}
	}
}

func BenchmarkInsertSortedIntSlice(b *testing.B) {
	fillMapSlice()
	b.ResetTimer()
	e := 2000
	val := fixString + strconv.Itoa(e)
	for n := 0; n < b.N; n++ {
		index := sort.Search(numItems, func(i int) bool {
			return sortedIntArr[i].key >= uint32(e)
		})
		copy(sortedIntArr[index+1:], sortedIntArr[index:])
		sortedIntArr[index].key = uint32(e)
		sortedIntArr[index].val = val
	}

}

func BenchmarkInsertIntMap(b *testing.B) {
	fillMapSlice()
	b.ResetTimer()
	e := 2000
	val := fixString + strconv.Itoa(e)
	for n := 0; n < b.N; n++ {
		intToStrMap[uint32(e)] = val
	}

}
