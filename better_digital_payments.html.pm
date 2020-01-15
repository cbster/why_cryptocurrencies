#lang pollen

◊(define-meta title "Better digital payments")
◊(define-meta subtitle "Benefits over existing payment systems")
◊(define-meta published "2019-06-03T00:00:00+01:00")
◊(define-meta updated "2020-01-15T20:08:14+01:00")
◊(define-meta uuid "011ff2b6-0e56-4501-a6ca-63e9ac6dcc65")

◊epigraph{
  ◊qt[#:author "Frank Underwood"
      #:src "House of Cards"]{
    When money is coming your way, you don't ask questions
  }
}

In this section we'll explore benefits cryptocurrencies have over other digital payment systems, such as VISA, Mastercard, PayPal or Apple Pay.

The big benefit is cryptocurrencies being ◊link[no-trusted-third-party]{◊em{permissionless}}: anyone can pay and anyone can accept them---for any business. Certain types of businesses, like pot stores or gambling sites, have problems accepting credit cards. Small businesses are also always at risk of having their accounts frozen without warning or recourse.◊sn{minecraft} Similarly there are people who cannot get bank accounts---and are in effect frozen out of large parts of the society.

But there are other benefits as well. Cryptocurrencies have lower fees and they drastically reduce and often eliminates the risk of charge back fraud---a big expense for merchants.

◊ndef["minecraft"]{
    When I say small business I do mean it. If PayPal freezes the account of a large or popular business, like ◊link[minecraft-paypal]{freezing the account of Minecraft (2010)}, the social backlash will make sure they're unblocked quickly. Small businesses---who can't gather outrage on social media---will simply be ignored.
}

◊(define minecraft-paypal "http://www.escapistmagazine.com/news/view/103385-PayPal-Freezes-750K-in-MineCraft-Devs-Account")
◊(define no-trusted-third-party "/properties_of_a_cryptocurrency.html#no-trusted-third-party")
