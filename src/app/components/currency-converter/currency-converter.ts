// src/app/components/currency-converter/currency-converter.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule, CurrencyPipe, KeyValuePipe } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../services/api';
import { debounceTime, distinctUntilChanged, switchMap, tap } from 'rxjs/operators';

// Import Angular Material Modules
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatIconModule } from '@angular/material/icon';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

@Component({
  selector: 'app-currency-converter',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatIconModule,
    MatProgressSpinnerModule,
    CurrencyPipe,
    KeyValuePipe
  ],
  templateUrl: './currency-converter.html',
  styleUrls: ['./currency-converter.css']
})
export class CurrencyConverterComponent implements OnInit {
  converterForm: FormGroup;
  currencies: { [key: string]: string } = {};
  convertedAmount: number | null = null;
  exchangeRate: number | null = null;
  isLoading = false;

  constructor(private fb: FormBuilder, private apiService: ApiService) {
    this.converterForm = this.fb.group({
      amount: [100],
      from: ['USD'],
      to: ['EUR']
    });
  }

  ngOnInit(): void {
    // 1. Fetch the list of currencies to populate dropdowns
    this.apiService.getCurrencies().subscribe(data => {
      this.currencies = data;
    });

    // 2. Listen for any change in the form's value
    this.converterForm.valueChanges.pipe(
      // Wait for 300ms after the user stops typing
      debounceTime(300),
      // Only proceed if the form value has actually changed
      distinctUntilChanged(),
      // Show loading spinner
      tap(() => { 
        this.isLoading = true;
        this.convertedAmount = null;
        this.exchangeRate = null;
      }),
      // Use switchMap to call the API with the new form values
      switchMap(formValue => 
        this.apiService.getExchangeRate(formValue.from, formValue.to)
      )
    ).subscribe(data => {
      const rate = data.rates[this.converterForm.value.to];
      const amount = this.converterForm.value.amount;

      this.exchangeRate = rate;
      this.convertedAmount = amount * rate;
      this.isLoading = false;
    });

    // 3. Trigger the first conversion when the component loads
    this.converterForm.updateValueAndValidity();
  }

  swapCurrencies(): void {
    const fromValue = this.converterForm.value.from;
    const toValue = this.converterForm.value.to;
    // Use patchValue to swap them, which will trigger the valueChanges listener
    this.converterForm.patchValue({ from: toValue, to: fromValue });
  }
}