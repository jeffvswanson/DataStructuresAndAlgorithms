package main

import (
	"bufio"
	"strings"
	"testing"
)

func TestGetNodeValue(t *testing.T) {
	mockUserInput := "150"
	reader := bufio.NewReader(strings.NewReader(mockUserInput))
	expected := 150

	got := getNodeValue("start")

	if got != expected {
		t.Errorf("Expected %d, got %v from getNodeValue(s string) int", expected, got)
	}
}
