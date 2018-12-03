use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() {
    let stdin = io::stdin();
    let vec = &mut Vec::new();
    vec.push(1 as usize);
    vec.push(1 as usize);
    for line in stdin.lock().lines(){
        let line = line.unwrap();
        let thresh = line.parse::<usize>().unwrap();
        let vec = calc_fib_vals(thresh,vec);
        println!("{}", vec[thresh]);
    }
    let write_file = File::create("FibOutput.txt");
    //now create the output string
    let mut i = 0 as usize;
    let mut output_str = String::new();
    while i < vec.len(){
        let index = i.to_string();
        let fib_val = vec[i].to_string();
        output_str.push_str(&index);
        output_str.push_str("          ");
        output_str.push_str(&fib_val);
        output_str.push('\n');
        i += 1;
    }
    write_file.unwrap().write(&(output_str.into_bytes()));
}

fn calc_fib_vals(threshold: usize, memos: &mut Vec<usize>) -> &mut Vec<usize>{
    let mut current = memos.len() - 1;
    while current < threshold{
        let next_fib = memos[current] + memos[current-1];
        memos.push(next_fib);
        current += 1;
    }
    memos
}
