class Torrent
  include Mongoid::Document

  field :title
  field :description
  field :link
  field :guid
  field :enclosure
  field :pub_date
end