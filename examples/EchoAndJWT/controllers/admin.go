package controllers

import (
	"github.com/labstack/echo/v4"
	"net/http"
)

func Admin() echo.HandlerFunc {
	return func(c echo.Context) error {
		return c.String(http.StatusOK, " OK")
	}
}
