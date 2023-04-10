from django.shortcuts import render
from math_test.services.eqgen import generate_eq
from math_test.services.wronggen import genwa
from django.http import JsonResponse
import json


# Create your views here.

def provide_page(request):
    return render(request, "math_test/index.html")

def get_quiz_test(request):
    jj = []
    jd = {
        "data": jj
    }
    for i in range(10):
        eq = generate_eq()
        wa = genwa(eq['ans1'], eq['ans2'])
        j = {
            "a": eq['a'],
            "b": eq['b'],
            "c": eq['c'],
            "correct1": eq['ans1'],
            "correct2": eq['ans2'],
            "wrong_answers": wa,
            "eq_str": f"{eq['a'] if eq['a'] != 1 else ''}x^2 {'+' if eq['b'] > 0 else '-'} {abs(eq['b']) if eq['b'] != 0 else ''}x {'+' if eq['c'] > 0 else '-'} {abs(eq['c'])} =0"
        }
        jj.append(j)
    return JsonResponse(jd)
    
