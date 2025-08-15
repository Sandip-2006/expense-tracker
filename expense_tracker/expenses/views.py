from django.shortcuts import render,redirect,get_object_or_404
from .models import Expense
from .forms import ExpenseForm

# Create your views here.

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    total = sum(e.amount for e in expenses)

    return render(request,'expenses/expense_list.html',{'expenses':expenses,'total':total})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'expenses/add_expense.html', {'form': form})

def delete_expense(request,expense_id):
    expense = get_object_or_404(Expense,id=expense_id)
    expense.delete()
    return redirect('expense_list')
