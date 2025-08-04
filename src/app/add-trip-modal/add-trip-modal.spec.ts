import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddTripModal } from './add-trip-modal';

describe('AddTripModal', () => {
  let component: AddTripModal;
  let fixture: ComponentFixture<AddTripModal>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AddTripModal]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddTripModal);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
