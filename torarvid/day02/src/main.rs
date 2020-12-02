use regex::Regex;
use std::format;
use std::fs;

fn main() {
    let filename = "input.txt";
    let contents =
        fs::read_to_string(filename).expect(&format!("Failed to read file {}", filename));
    let lines = contents.split('\n').collect();
    println!("Part1: {}", solve_part1(&lines));
    println!("Part2: {}", solve_part2(&lines));
}

fn solve_part1(input: &Vec<&str>) -> i32 {
    let re = Regex::new(r"^(\d+)-(\d+) (.): (.+)$").unwrap();
    let mut valid: i32 = 0;
    for line in input {
        for cap in re.captures_iter(line) {
            let min = cap[1].parse::<usize>().unwrap();
            let max = cap[2].parse::<usize>().unwrap();
            let character = &cap[3];
            let password = &cap[4];
            let count = password.matches(character).count();
            if count >= min && count <= max {
                valid += 1;
            }
        }
    }
    valid
}

fn solve_part2(input: &Vec<&str>) -> i32 {
    let re = Regex::new(r"^(\d+)-(\d+) (.): (.+)$").unwrap();
    let mut valid: i32 = 0;
    for line in input {
        for cap in re.captures_iter(line) {
            let first = cap[1].parse::<usize>().unwrap();
            let second = cap[2].parse::<usize>().unwrap();
            let character = cap[3].chars().nth(0).unwrap();
            let password = &cap[4];
            let first_matches = password.chars().nth(first - 1).unwrap() == character;
            let second_matches = password.chars().nth(second - 1).unwrap() == character;
            if first_matches ^ second_matches {
                valid += 1;
            }
        }
    }
    valid
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve_part1() {
        assert_eq!(
            solve_part1(
                &String::from(
                    "1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"
                )
                .split('\n')
                .collect()
            ),
            2,
        );
    }

    #[test]
    fn test_solve_part2() {
        assert_eq!(
            solve_part2(
                &String::from(
                    "1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"
                )
                .split('\n')
                .collect()
            ),
            1,
        );
    }
}
