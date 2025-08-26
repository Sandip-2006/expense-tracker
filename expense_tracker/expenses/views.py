from django.shortcuts import render,redirect,get_object_or_404
from .models import Expense
from .forms import ExpenseForm,SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(redirect_field_name='next',login_url='login')
def expense_list(request):
    user = request.user
    expenses = Expense.objects.filter(user = user).order_by('-date')
    total = sum(e.amount for e in expenses)

    return render(request,'expenses/expense_list.html',{'expenses':expenses,'total':total})

@login_required(redirect_field_name='next',login_url='login')
def add_expense(request):
    user = request.user
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)  
            expense.user = request.user   # 👈 current user assign
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'expenses/add_expense.html', {'form': form})

def delete_expense(request,expense_id):
    expense = get_object_or_404(Expense,id=expense_id)
    expense.delete()
    return redirect('expense_list')

def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_superuser or user.is_staff:
                    messages.error(request, "Admin users are not allowed to login here.")
                    return redirect("login")  # ya wahi page reload
                login(request,user)
                return redirect('add_expense')
            else:
                messages.error(request, "Invalid username or password")
            
    else:
        form = AuthenticationForm()
    return render(request,'expenses/login.html',{'form':form})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect("login")   # login page ka name url.py me "login" hona chahiye
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, "expenses/signup.html", {"form": form})

def logoutView(request):
    logout(request)
    return redirect('login')