package main

// The bunny bandit in the terminal (Chief 10/18): boot.py's shrink of the ASCII mark, then the hackerpunk entrance.
// The glyphs decode out of noise, the head spins on its vertical axis and holds front-on between turns,
// and now and then a few rows tear sideways.

import (
	"math"
	"math/rand"
	"os"
	"strings"
	"time"
)

const ramp = " .-+#"

func loadArt(path string) []string {
	b, err := os.ReadFile(path)
	if err != nil {
		return nil
	}
	var rows []string
	for _, l := range strings.Split(strings.ReplaceAll(string(b), "\r", ""), "\n") {
		if strings.TrimSpace(l) != "" {
			rows = append(rows, strings.TrimRight(l, " "))
		}
	}
	ind := 1 << 30
	for _, l := range rows {
		if n := len(l) - len(strings.TrimLeft(l, " ")); n < ind {
			ind = n
		}
	}
	for i := range rows {
		rows[i] = rows[i][ind:]
	}
	return rows
}

// shrink keeps the densest character of each scale x scale block, as boot.py does
func shrink(rows []string, scale int) []string {
	if scale < 1 {
		scale = 1
	}
	w := 0
	for _, l := range rows {
		if len(l) > w {
			w = len(l)
		}
	}
	at := func(y, x int) byte {
		if x < len(rows[y]) {
			return rows[y][x]
		}
		return ' '
	}
	var out []string
	for y := 0; y < len(rows); y += scale {
		var sb strings.Builder
		for x := 0; x < w; x += scale {
			best := byte(' ')
			for yy := y; yy < y+scale && yy < len(rows); yy++ {
				for xx := x; xx < x+scale && xx < w; xx++ {
					if c := at(yy, xx); strings.IndexByte(ramp, c) > strings.IndexByte(ramp, best) {
						best = c
					}
				}
			}
			sb.WriteByte(best)
		}
		out = append(out, strings.TrimRight(sb.String(), " "))
	}
	return out
}

type spinner struct {
	g       []string
	w, h    int
	seed    [][]float64
	t0      time.Time
	glUntil time.Time
	nextGl  time.Time
	glRows  map[int]int
	rng     *rand.Rand
}

func newSpinner(rows []string) *spinner {
	s := &spinner{h: len(rows), t0: time.Now(), rng: rand.New(rand.NewSource(time.Now().UnixNano()))}
	for _, l := range rows {
		if len(l) > s.w {
			s.w = len(l)
		}
	}
	for _, l := range rows {
		s.g = append(s.g, l+strings.Repeat(" ", s.w-len(l)))
		r := make([]float64, s.w)
		for i := range r {
			r[i] = s.rng.Float64()
		}
		s.seed = append(s.seed, r)
	}
	s.nextGl = s.t0.Add(1800 * time.Millisecond)
	return s
}

func easeInOut(p float64) float64 {
	if p < .5 {
		return 4 * p * p * p
	}
	return 1 - math.Pow(-2*p+2, 3)/2
}

const noise = "!<>-_\\/[]{}=+*^?#01"

var backFace = map[byte]byte{'#': '+', '+': '-', '-': '.', '.': '.'}

// frame draws the mark at this instant; still=true gives the plain front face
func (s *spinner) frame(now time.Time, still bool) string {
	t := now.Sub(s.t0).Seconds()
	dec, th := 1.0, 0.0
	if !still {
		dec = math.Min(1, t/1.1)
		if t > 1.3 {
			p := math.Mod(t-1.3, 5) / 5
			if p >= .4 {
				th = easeInOut((p-.4)/.6) * 2 * math.Pi
			}
		}
		if now.After(s.nextGl) {
			s.glUntil = now.Add(130 * time.Millisecond)
			s.glRows = map[int]int{}
			for k := 0; k < 3; k++ {
				sh := 2 + s.rng.Intn(4)
				if s.rng.Intn(2) == 0 {
					sh = -sh
				}
				s.glRows[s.rng.Intn(s.h)] = sh
			}
			s.nextGl = now.Add(time.Duration(1500+s.rng.Intn(2500)) * time.Millisecond)
		}
	}
	c := math.Cos(th)
	cx := float64(s.w-1) / 2
	lines := make([]string, s.h)
	for y := 0; y < s.h; y++ {
		sh := 0
		if !still && now.Before(s.glUntil) {
			sh = s.glRows[y]
		}
		var out strings.Builder
		var buf strings.Builder
		cls := byte(0)
		flush := func() {
			if buf.Len() == 0 {
				return
			}
			if st, ok := shade[cls]; ok {
				out.WriteString(st.Render(buf.String()))
			} else {
				out.WriteString(buf.String())
			}
			buf.Reset()
		}
		for ox := 0; ox < s.w; ox++ {
			ch, k := byte(' '), byte(0)
			if math.Abs(c) < 0.03 {
				if ox == int(math.Round(cx)) && strings.TrimSpace(s.g[y]) != "" {
					ch, k = '|', 'p'
				}
			} else {
				sx := int(math.Round(cx + (float64(ox-sh)-cx)/c))
				if sx >= 0 && sx < s.w {
					ch = s.g[y][sx]
					if b, ok := backFace[ch]; ok && c < 0 {
						ch = b
					}
				}
				if ch != ' ' {
					switch {
					case dec < 1 && s.seed[y][sx] > dec:
						ch, k = noise[s.rng.Intn(len(noise))], 'z'
					case sh != 0:
						k = 'g'
					default:
						k = ch
					}
				}
			}
			if k != cls {
				flush()
				cls = k
			}
			buf.WriteByte(ch)
		}
		flush()
		lines[y] = out.String()
	}
	return strings.Join(lines, "\n")
}
