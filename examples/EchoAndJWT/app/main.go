package main

import (
	"EchoJWT/controllers"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {
	e := echo.New()

	e.Use(middleware.Logger())

	adminGroup := e.Group("/admin")
	adminGroup.GET("", controllers.Admin())

	// Start Echo
	e.Logger.Fatal(e.Start(":8080"))

}
