// src/app/components/financial-summary/financial-summary.ts
import { Component, Input } from '@angular/core';
import { CommonModule, CurrencyPipe } from '@angular/common';
import { Trip } from '../../models/trip.model';

import { MatCardModule } from '@angular/material/card';
import { MatDividerModule } from '@angular/material/divider';

@Component({
  selector: 'app-financial-summary',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatDividerModule, CurrencyPipe],
  templateUrl: './financial-summary.html',
  styleUrls: ['./financial-summary.css']
})
export class FinancialSummaryComponent {
  @Input() trip: Trip | null = null;
}