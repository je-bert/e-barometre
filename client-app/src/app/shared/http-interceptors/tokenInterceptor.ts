import { Injectable } from "@angular/core";

import {
    HttpEvent,
    HttpInterceptor,
    HttpHandler,
    HttpRequest
} from '@angular/common/http'

import { Observable } from "rxjs";

@Injectable()
export class TokenInterceptor implements HttpInterceptor {
    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        const token = window.localStorage.getItem('token')

        if (!token) return next.handle(req)

        const cloned = req.clone({
            headers: req.headers.set('x-access-token', token)
        })

        return next.handle(cloned)
    }
}