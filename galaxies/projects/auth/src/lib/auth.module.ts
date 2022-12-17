import { NgModule } from '@angular/core';
import { TranslateModule } from '@ngx-translate/core';

import { UiModule } from '@ui';

import { AuthComponent } from './auth.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';

@NgModule({
  declarations: [
    AuthComponent,
    LoginComponent,
    RegisterComponent
  ],
  imports: [
    TranslateModule,
    UiModule
  ],
  exports: [
    AuthComponent
  ]
})
export class AuthModule { }
