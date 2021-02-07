import discord
from discord.ext import commands
from discord.utils import get
import random
import os
import youtube_dl
from datetime import datetime
import sympy
from sympy.solvers import solve
from sympy import *
from PIL import Image
from io import BytesIO

size = '600'



client = commands.Bot(command_prefix= '!', case_insensitive=True)
x, y, z = symbols('x y z')


@client.event
async def on_ready():
    print('Bot is ready')

@client.command(help = 'Solves algebra', aliases = ['solve'])
async def solveequa(ctx, *, equa):
    eq = str(equa).replace('\*','*')
    eq = sympy.sympify(eq)
    solutions = solve(eq, x)
    for solution in solutions:
        obj = BytesIO()
        preview(solution, output='png', viewer='BytesIO', outputbuffer=obj, dvioptions=['-D', size], euler=False)
        obj.seek(0)
        img = discord.File(obj, filename='result.png')
        print(solution)
        await ctx.send(file=img)


@client.command(help = 'Solves derivatives', aliases = ['diff'])
async def differentiate(ctx, equa, *, differentials):
    differentials = str(differentials)
    differentials = [sympy.Symbol(s) for s in differentials.split(' ')]
    solution = diff(equa, *differentials)
    obj = BytesIO()
    preview(solution, output='png', viewer='BytesIO', outputbuffer=obj, dvioptions=['-D', size], euler=False)
    obj.seek(0)
    img = discord.File(obj, filename='result.png')
    print(solution)
    await ctx.send(file=img)

@client.command(help = 'Solves indefinite integrals', aliases = ['int'])
async def indeff_integrate(ctx, *, equa):
    equa = sympy.sympify(equa)
    solution = integrate(equa, x)
    obj = BytesIO()
    preview(solution, output='png', viewer='BytesIO', outputbuffer=obj, dvioptions=['-D', size], euler=False)
    obj.seek(0)
    img = discord.File(obj, filename='result.png')
    print(solution)
    await ctx.send(file=img)

@client.command(help = 'Solves definite integrals')
async def defint(ctx, *, equa):
    lower_bound = str(equa).split(' ')[1]
    upper_bound =str(equa).split(' ')[2]
    equa = str(equa).split(',')[0]
    solution = integrate(equa,(x,lower_bound,upper_bound))
    obj = BytesIO()
    preview(solution, output='png', viewer='BytesIO', outputbuffer=obj, dvioptions=['-D', size], euler=False)
    obj.seek(0)
    img = discord.File(obj, filename='result.png')
    print(solution)
    await ctx.send(file=img)

@client.command(help = 'Simplifies algebra', aliases =['simplify'])
async def _simplify(ctx, *, equa):
    eq = str(equa)
    eq = sympy.sympify(eq)
    solution = simplify(eq)
    obj = BytesIO()
    preview(solution, output='png', viewer='BytesIO', outputbuffer=obj, dvioptions=['-D', size], euler=False)
    obj.seek(0)
    img = discord.File(obj, filename='result.png')
    print(solution)
    await ctx.send(file=img)

@client.command(help = 'expands', aliases =['expand'])
async def _expand(ctx, *, equa):
    equa = sympy.sympify(equa)
    solution = sympy.expand(equa)
    obj = BytesIO()
    preview(solution, output='png', viewer='BytesIO', outputbuffer=obj, dvioptions=['-D', size], euler=False)
    obj.seek(0)
    img = discord.File(obj, filename='result.png')
    print(solution)
    await ctx.send(file=img)

@client.command(help = 'factorizes', aliases =['factor','factorise'])
async def factorize(ctx, *, equa):
    equa = sympy.sympify(equa)
    solution = sympy.factor(equa)
    obj = BytesIO()
    preview(solution, output='png', viewer='BytesIO', outputbuffer=obj, dvioptions=['-D', size], euler=False)
    obj.seek(0)
    img = discord.File(obj, filename='result.png')
    print(solution)
    await ctx.send(file=img)


client.run('')
