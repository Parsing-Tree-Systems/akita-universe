import { NgModule } from '@angular/core';

import { ReactiveFormsModule } from '@angular/forms';

import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule, MAT_FORM_FIELD_DEFAULT_OPTIONS } from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';


import { UiComponent } from './ui.component';

export const MaterialModules = [
  MatCardModule,
  MatFormFieldModule,
  MatIconModule
];

@NgModule({
  declarations: [
    UiComponent
  ],
  providers: [
    {provide: MAT_FORM_FIELD_DEFAULT_OPTIONS, useValue: {appearance: 'outline'}}
  ],
  imports: [
    ReactiveFormsModule,
    ...MaterialModules
  ],
  exports: [
    UiComponent,
    ...MaterialModules
  ]
})
export class UiModule { }
